from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
from .models import Member


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
    
  }
  return HttpResponse(template.render(context, request))

 
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def images(request):
     templates = loader.get_template('images.html')
     return HttpResponse(templates.render())

def chat(request):
     templates = loader.get_template('chat.html')
     return HttpResponse(templates.render())

def videos(request):
     templates = loader.get_template('videos.html')
     return HttpResponse(templates.render())

def maps(request):
     templates = loader.get_template('maps.html')
     return HttpResponse(templates.render())

def news(request):
     templates = loader.get_template('news.html')
     return HttpResponse(templates.render())


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
