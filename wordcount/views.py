from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'wordcount/home.html')


def about(request):
    return render(request, 'wordcount/about.html')


def count(request):
    return render(request,'wordcount/count.html')   

