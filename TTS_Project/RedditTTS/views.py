from django.shortcuts import render,redirect
from . import redditTTS

rTTS = None
queue=[]

# Create your views here.
def select_posts(request):
    global rTTS
    global queue
    args = {'queue':queue}

    if request.method=="POST":
        post = rTTS.getFromURL(request.POST["reddit_url"])
        args['queue'].append(post)
    else:
        rTTS = redditTTS.RedditTTS()
        rTTS.create()
    return render(request, 'select_posts.html', args)

def gen_video(request):
    rTTS.generate()
    return redirect('home')