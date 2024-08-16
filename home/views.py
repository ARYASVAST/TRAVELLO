from enum import member
from django.shortcuts import render, HttpResponse
from django.template import loader



from django.http import HttpResponse

def home(request):
 
    peoples = [
        {'name' : 'Abhijeet', 'age' : 26},
        {'name' : 'Rohan Sharma', 'age' : 23},
        {'name' : 'Vicky Kaushal', 'age' : 24},
        {'name' : 'Sandeep', 'age' : 25},
        {'name' : 'Deepanshu', 'age' : 29},
    ]

    

    return render(request , "home/index.html", context = {'peoples' : peoples})

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a success page.</hl>")


def testing(request):
    template = loader.get_template('home/template.html')
    context = {
    'greeting' : 1,
    'fruits': ['Apple', 'Banana', 'Cherry', 'Oranges', 'Kiwi'], 
    
  }
    return HttpResponse(template.render(context, request))






# background
