from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.
from .import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'