from django.shortcuts import render

# Create your views here.
def user_account(request,username):
    return render(request,'UserAccount.html')