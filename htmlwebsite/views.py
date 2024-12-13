from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return render(request,'index.html')
def signin(request):
    return render(request,'signin.html')
def vote(request):
    return render(request,'vote.html')

