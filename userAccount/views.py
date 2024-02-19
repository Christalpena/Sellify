from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def user_account(request,username):
    print(request.user.profile_photo)
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print("Holaa")
        if form.is_valid():
            print("holaaa")
    return render(request,'UserAccount.html',{'form':form})