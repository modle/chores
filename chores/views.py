from chores.forms import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db import IntegrityError
import re
from django.contrib import messages
import math
import pytz

from chores.models import Chores, Category, History, Score


@login_required()
def index(request):

    return HttpResponseRedirect(reverse('profile', args=[request.user]))


@login_required()
def all_chores(request):

    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            search_term = search_form.cleaned_data['search_term']

            chores = Chores.objects.filter(title__icontains=search_term)
        else:
            chores = Chores.objects.all()
    else:
        chores = Chores.objects.all()

    return render_to_response('all_chores.html', {
        'chores': chores,
        'search_form': search_form,
        },
        context_instance=RequestContext(request)
    )


@login_required()
def clear_all_chores_filter(request):

    return HttpResponseRedirect(reverse('all_chores'))


@login_required()
def clear_view_history_filter(request):

    return HttpResponseRedirect(reverse('view_chores_history'))


@login_required()
def all_categories(request):

    category_form = CategoryForm()
    categories = category_count()

    if request.method == 'POST':
        category_form = CategoryForm(request.POST)

        if category_form .is_valid():
            category_form.save()

    return render_to_response('all_categories.html', {
        'categories': categories,
        'category_form': category_form,
        },
        context_instance=RequestContext(request)
    )


@login_required()
def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    chores = Chores.objects.all()

    return render_to_response('view_category.html', {
        'category': category,
        'chores': chores,
    },

        context_instance=RequestContext(request)
    )


@login_required()
def delete_category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    category.delete()
    return HttpResponseRedirect(reverse('all_categories'))


def category_count():
    categories = Category.objects.extra(select={'total': 'select count(c.category_id) ' +
                                                         'from chores_chores c ' +
                                                         'where c.category_id = chores_category.id '
                                                })
    return categories


@login_required()
def rewards(request):

    rewards_form = RewardsForm()
    rewards_set = Rewards.objects.all()

    try:
        score = Score.objects.get(user=request.user)
    except Score.DoesNotExist:
        score = Score.objects.filter(user=request.user)

    if request.method == 'POST':
        rewards_form = RewardsForm(request.POST)

        if rewards_form .is_valid():
            rewards_form.save()
            rewards_set = Rewards.objects.all()
            rewards_form = RewardsForm()

    return render_to_response('rewards.html', {
        'rewards_set': rewards_set,
        'rewards_form': rewards_form,
        'score': score,
        },
        context_instance=RequestContext(request)
    )


@login_required()
def delete_reward(request, slug):
    reward = get_object_or_404(Rewards, slug=slug)

    reward.delete()
    return HttpResponseRedirect(reverse('rewards'))


@login_required()
def redeem_reward(request, slug):

    try:
        score = Score.objects.get(user=request.user)
    except Score.DoesNotExist:
        messages.error(request, 'You don''t have any points!')
        return HttpResponseRedirect(reverse('rewards'))

    s = get_object_or_404(Score, user=request.user)
    r = get_object_or_404(Rewards, slug=slug)

    if s.current_score >= r.value:
        s.current_score -= r.value
        s.last_redeemed_date = timezone.now()
        s.save()

        r.last_redeemed_date = timezone.now()
        r.last_redeemed_by = request.user
        r.save()

        messages.success(request, r.title + ' redeemed for ' + str(r.value) + ' points!')

    else:
        messages.error(request, 'You need ' + str(r.value - s.current_score) + ' more points for ' + r.title)

    return HttpResponseRedirect(reverse('rewards'))


@login_required()
def profile(request, slug):
    user = request.user

    if request.method == 'POST':
        form = ChoresForm(request.POST)

        if form.is_valid():

            formpost = form.save(commit=False)
            new_chore = formpost.title
            new_chore_category = formpost.category

            # prevents error on duplicate, but would also like to pass message to profile view
            try:
                formpost.save()
                messages.success(request, new_chore + ' added for category ' + str(new_chore_category) + '!')
                return HttpResponseRedirect(reverse('profile', args=[request.user]))

            except IntegrityError as e:
                if 'duplicate key' in str(e):
                    messages.error(request, new_chore + ' already exists for category ' + str(new_chore_category) + '!')

        else:
            messages.error(request, 'Please correct the indicated form errors.')

    else:
        form = ChoresForm()

    chores = Chores.objects.filter(primary_assignee=user.id)
    score = Score.objects.filter(user=user.id)

    return render_to_response('profile.html', {
        'chores': chores,
        'form': form,
        'score': score,
        },
        context_instance=RequestContext(request)
    )


@login_required()
def view_chores_history(request):
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            search_term = search_form.cleaned_data['search_term']

            chores_history = History.objects.filter(chore__title__icontains=search_term)
        else:
            chores_history = History.objects.all()
    else:
        chores_history = History.objects.all()

    return render_to_response('view_chores_history.html', {
        'chores_history': chores_history,
        'search_form': search_form,
    },

        context_instance=RequestContext(request)
    )


@login_required()
def edit_chore(request, slug):
    # successful form save = redirect to all chores
    # unsuccessful = redirect to edit chore
    if request.method == 'POST':
        form = ChoresForm(request.POST, instance=Chores.objects.get(slug=slug))

        if form.is_valid():
            formpost = form.save(commit=False)
            formpost.user = request.user
            formpost.save()
            return HttpResponseRedirect(reverse('all_chores'))

    chore = Chores.objects.get(slug=slug)
    form = ChoresForm(instance=chore)

    return render_to_response('edit_chore.html', {'form': form, },
                              context_instance=RequestContext(request))


@login_required()
def mark_chore_done(request, slug):
    # if chore completed by someone other than primary - then done from all-chores page, so redirect there
    # if chore completed by primary, redirect to profile
    chore = get_object_or_404(Chores, slug=slug)

    utc = pytz.UTC
    td = timezone.now() - chore.last_completed_date

    if td.days >= chore.frequency_in_days:

        chore.last_completed_date = timezone.now().replace(tzinfo=utc)
        chore.last_completed_by_id = request.user
        chore.save()

        score_value = math.ceil(chore.time_in_minutes*chore.effort/10.0)

        h = History(chore=chore, completed_date=timezone.now(), user=request.user, score=score_value,)
        h.save()

        score, created = Score.objects.get_or_create(user=request.user)
        score.current_score += score_value
        score.total_score += score_value
        score.save()

        messages.success(request, 'Chore ' + chore.title + ' for category ' + str(chore.category) +
                         ' marked done!')
        messages.info(request, str(int(score_value)) + ' point(s)!')

    else:
        messages.error(request, 'Chore ' + chore.title + ' not marked done. It was too recently completed.')

    referer = request.META.get('HTTP_REFERER')
    referer = re.sub('^https?:\/\/', '', referer).split('/')
    redirect = referer[2].replace('.html','')

    if redirect == 'all_chores':
        return HttpResponseRedirect(reverse(redirect))
    else:
        return HttpResponseRedirect(reverse(redirect, args=[request.user]))


def notauthorized(request):
    return render_to_response(
        'registration/not_authorized.html',
        context_instance=RequestContext(request)
    )


def loggedin(request):
    return render_to_response(
        'registration/loggedin.html',
        context_instance=RequestContext(request)
    )


def loggedout(request):
    return render_to_response(
        'registration/loggedout.html',
        context_instance=RequestContext(request)
    )
