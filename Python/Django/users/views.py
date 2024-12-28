from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """Faz um logout do usuário."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    