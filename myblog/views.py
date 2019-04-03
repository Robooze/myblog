from django.http import HttpResponse
from django.shortcuts import render

# Callback functions fired when relative URL's are requested
def homepage(request):  
    # return HttpResponse('homepage')
    return render(request,'homepage.html')


def about(request):
    # return HttpResponse('about')
    return render(request,'about.html')
