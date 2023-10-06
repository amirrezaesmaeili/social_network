from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterationForm
from django.contrib.auth.models import User
from django.contrib import messages

class RegisterationView(View):
    form_class = RegisterationForm
    template_name = 'account/register.html'

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd["user_name"] , cd["email"] , cd["password1"])
            messages.success(request , "your registerd successfuly" , "success")
            return redirect("home:home")
        return render(request,self.template_name,{"form":form})
