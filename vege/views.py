#from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from .models import *

def receipes(request):
  if request.method =="POST": 

    data = request.POST 
    receipe_name = data.get('receipe_name')
    receipe_description = data.get('receipe_description')
    receipe_image = request.FILES.get('receipe_image')

    Receipe.objects.create(
      receipe_name = receipe_name ,
      receipe_description = receipe_description,
      receipe_image = receipe_image,
    )

  
  queryset = Receipe.objects.all()
  context = {'receipes': queryset}
  return render(request , 'receipes.html', context)