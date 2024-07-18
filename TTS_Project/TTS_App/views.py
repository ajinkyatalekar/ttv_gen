from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    args = {}
    if request.user.is_authenticated:
        return redirect('logged_in_home')
    else:
        return render(request, 'home/index.html', args)

def logged_in_home(request):
    args = {}

    if request.user.is_authenticated:
        return render(request, 'home/logged_in_home.html', args)
    else:
        return redirect('home')

def about(request):
    args = {}

    return render(request, 'home/about.html', args)