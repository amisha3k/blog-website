#from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render

def about(request):
    social_links = settings.SOCIAL_MEDIA_LINKS  # Retrieve from settings
    return render(request, "about.html", {"social_links": social_links})


def homepage(request):
   # return HttpResponse("hello, this is homepage")
   return render(request, 'home.html')

def about(request):
  #  return HttpResponse("my about")   
  return render(request, 'about.html')