from django.shortcuts import render
from django.views import View
from .forms import RegisterationForm

class RegisterationView(View):
    def get(self,request):
        form = RegisterationForm()
        return render(request,'account/register.html',{'form':form})
    
    def post(self,request):
        pass