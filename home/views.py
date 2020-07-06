from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request,'home/base.html')
def select(request):
    return render(request,'home/select.html')
class SignupView(generic.CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy('login')
    template_name='home/signup.html'
    context_object_name='tt'

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import SignUpForm
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})