from chores.forms import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
from django.utils.text import slugify
import itertools


from chores.models import Chores, Category, History


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
def profile(request, slug):
    user = request.user

    if request.method == 'POST':
        form = ChoresForm(request.POST)

        if form.is_valid():

            formpost = form.save(commit=False)
            original = slugify(formpost.title)

            for x in itertools.count(1):
                if not Chores.objects.filter(slug=slug).exists():
                    break
                slug = '{}-{}'.format(original, x)

            formpost.save()

        return HttpResponseRedirect(reverse('profile', args=[request.user]))

    else:
        form = ChoresForm()

    chores = Chores.objects.filter(primary_assignee=user.id)

    return render_to_response('profile.html', {
        'chores': chores,
        'form': form,
        },
        context_instance=RequestContext(request)
    )


@login_required()
def edit_chore(request, slug):
    if request.method == 'POST':
        form = ChoresForm(request.POST, instance=Chores.objects.get(slug=slug))

        if form.is_valid():
            formpost = form.save(commit=False)
            formpost.user = request.user
            formpost.edited = datetime.now()
            formpost.save()

        chore = Chores.objects.get(slug=slug)
        form = ChoresForm(instance=chore)

    else:
        chore = Chores.objects.get(slug=slug)
        form = ChoresForm(instance=chore)

    return render_to_response('edit_chore.html', {'form': form, },
                              context_instance=RequestContext(request))


@login_required()
def mark_chore_done(request, slug):
    chore = get_object_or_404(Chores, slug=slug)

    chore.last_completed_date = datetime.now()
    chore.save()

    h = History(chore=chore, complete_date=datetime.now(), user=request.user)
    h.save()

    return HttpResponseRedirect(reverse('profile', args=(request.user,)))


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
