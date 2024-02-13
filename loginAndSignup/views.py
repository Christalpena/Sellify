from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import CustomUserCreationForm,CompleteProfileForm
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ValidationError
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

class SignUp(View):
    form = CustomUserCreationForm
    
    def get(self,request):
        form = self.form
        return render(request,'./SignUp.html',{'form':form})

    def post(self,request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save(commit=False)
            request.session['email'] = form.cleaned_data['email']
            request.session['password'] = form.cleaned_data['password1']

            return redirect('complete_profile')
        else:
            return render(request,'./SignUp.html',{'form':form})
        
class CompleteProfile(View):
    form = CompleteProfileForm

    def get(self,request):
        if request.user.is_active or request.user.username:
            return redirect('Feed')

        else:
            form = self.form
            return render(request, 'CompleteSignUp.html', {'form': form})
    
    def post(self,request):
        user_email = request.session.get('email')
        password = request.session.get('password')

        if not user_email:
            return redirect('signUp')

        if request.method == 'POST':
            form = self.form(request.POST)
            user = CustomUser.objects.filter(username = request.POST['username'])
            if form.is_valid() and not user:
                try:
                    new_user = CustomUser.objects.create_user(
                    username = form.cleaned_data['username'],
                    email = user_email,
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name'],
                    password = password
                    )
                
                    user = authenticate(username = form.cleaned_data['username'],
                    password=password)
                    
                    if user is not None:
                        login(request,user)
                        return redirect('Feed')
                except:
                    raise ValidationError("Something went wrong")
            else:
                return render(request, 'CompleteSignUp.html', {'form': form})
    
def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('Feed')
            else:
                print("holaa")
                form.add_error(None, "Invalid credentials provided.")
    return render(request, 'Login.html',{'form':form})  
      
def logout_view(request):
    logout(request)
    return redirect('signUp')