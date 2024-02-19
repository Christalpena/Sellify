from django.shortcuts import redirect, render
from .forms import PostForm

# Create your views here.
def user_account(request,username):
    print(request.user.profile_photo)
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(f'/user/{request.user.username}')
        else:
            form = PostForm(request.POST, request.FILES)
    return render(request,'UserAccount.html',{'form':form})