from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterationForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate

class UserRegisterView(View):
    form_class = RegisterationForm
    template_name = 'account/register.html'

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd["username"] , cd["email"] , cd["password1"])
            messages.success(request , "your registerd successfuly" , "success")
            return redirect("home:home")
        return render(request,self.template_name,{"form":form})


class UserLoginView(View):
    form_class = LoginForm
    template_name = "account/login.html"


    def get(self,request):
        form = self.form_class 
        return render(request , self.template_name , {'form':form} )

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate( request , username=cd["username"], password=cd["password"] )
            if user is not None:
                login(request,user)
                messages.success(request , "you login successfuly" , "success")
                return redirect("home:home")
            messages.error(request , "password or username not correct" 'warning')
        return render(request ,self.form_class,{'form':form})
    
    



        