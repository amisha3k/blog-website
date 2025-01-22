#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
   # return HttpResponse("hello, this is homepage")
   return render(request, 'home.html')

def about(request):
  #  return HttpResponse("my about")   
  return render(request, 'about.html')