from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(
        request,
        'portfolio/home.html',
       
    )
def projects(request):
      return render(
        request,
        'portfolio/projects.html',
       
    )
    
def blog(request):
      return render(
        request,
        'portfolio/blog.html',
       
    )
   



