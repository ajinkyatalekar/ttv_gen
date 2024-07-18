from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    args = {}
    return render(request, 'home/index.html', args)

def about(request):
    args = {}
    return render(request, 'home/about.html', args)