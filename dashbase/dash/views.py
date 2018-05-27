from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
