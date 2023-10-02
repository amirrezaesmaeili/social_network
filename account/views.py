from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterationForm
from django.contrib.auth.models import User
from django.contrib import messages

class RegisterationView(View):
    def get(self,request):
        form = RegisterationForm()
        return render(request,'account/register.html',{'form':form})
    
    def post(self,request):
        form = RegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd["user_name"] , cd["email"] , cd["password"])
            messages.success(request , "your registerd successfuly" , "success")
            return redirect("home:home")
