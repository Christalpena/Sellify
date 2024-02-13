from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def Feed(request):
    return render(request, './Feed.html')

def Feed_redirect(request):
    return redirect('Feed')