from django.shortcuts import render,redirect

# Create your views here.


def Feed(request):
    return render(request, './Feed.html')

def Feed_redirect(request):
    return redirect('Feed')