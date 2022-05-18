from .models import Tweep
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


class TweepCreate(CreateView):
  model = Tweep
  fields = '__all__'
  success_url = '/tweeps/'

class TweepUpdate(UpdateView):
  model = Tweep
  fields = ['description', 'recipe']

class TweepDelete(DeleteView):
  model = Tweep
  success_url = '/tweeps/'

def tweeps_by_tag(request, tag_slug):
  tweeps = Tweep.objects.filter(tags__name__in=[tag_slug])
  return render(request, 'tweeps/index.html', {'tweeps': tweeps, 'tag': tag_slug})

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tweeps_index(request):
  tweeps = Tweep.objects.all()
  return render(request, 'tweeps/index.html', { 'tweeps': tweeps })

def tweeps_detail(request, tweep_id):
  tweep = Tweep.objects.get(id=tweep_id)
  return render(request, 'tweeps/detail.html', { 'tweep': tweep})

def tweep_search(request):
  if request.method == "POST":
    searched = request.POST['searched']
    tweeps = Tweep.objects.filter(name__contains=searched)
    return render(request, 'main_app/tweep_search.html', {'searched':searched, 'tweeps':tweeps})
  else:
    return render(request, 'main_app/tweep_search.html', {})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - Please try again.'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


# def login(request):
#   error_message = ''
#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       login(request, user)
#       return redirect('home')
#     else:
#       error_message = 'Invalid sign up - Please try again.'
#   form = UserCreationForm()
#   context = {'form': form, 'error_message': error_message}
#   return render(request, 'registration/login.html', context)