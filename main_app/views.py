import imp
from .models import Tweep
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import os
import uuid
import boto3
# from .models import profile, Photo


class TweepCreate(CreateView):
  model = Tweep
  fields = '__all__'
  success_url = '/tweeps/'

class TweepUpdate(UpdateView):
  model = Tweep
  fields = ['tweeps']

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

def profile(request):
  return render(request, 'profile.html')

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

@login_required
def add_photo(request, tweep_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, tweep_id=tweep_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', tweep_id=tweep_id)