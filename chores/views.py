from chores.forms import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from datetime import datetime
from django.utils.text import slugify
import itertools


from chores.models import Chores, Category, History


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def index(request):

    return HttpResponseRedirect(reverse('profile', args=[request.user]))
    # chores = Chores.objects.all()
    # search_form = SearchForm()
    #
    # return render_to_response('index.html', {
    #     'chores': chores,
    #     'search_form': search_form,
    #     },
    #     context_instance=RequestContext(request)
    # )


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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()

    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response(
        'registration/registration_form.html',
        token,
        context_instance=RequestContext(request)
    )


def registration_complete(request):
    return render_to_response(
        'registration/registration_complete.html',
        context_instance=RequestContext(request)
    )


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


def search(request):

    if request.method == 'POST':
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            search_term = search_form.cleaned_data['search_term']

            chores = Chores.objects.filter(title__icontains=search_term)

            return render_to_response('search_results.html', {
                'chores': chores,
            },
                context_instance=RequestContext(request)
            )

    chores = Chores.objects.all()

    return render_to_response('index.html', {
        'chores': chores,
        },
        context_instance=RequestContext(request)
    )


def mark_chore_done(request, slug):
    chore = get_object_or_404(Chores, slug=slug)

    chore.last_completed_date = datetime.now()
    chore.save()

    h = History(chore=chore, complete_date=datetime.now(), user=request.user)
    h.save()

    return HttpResponseRedirect(reverse('profile', args=(request.user,)))
