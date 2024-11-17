from django.shortcuts import render


def index(request):
    """Página Principal do Learn_Log"""
    return render(request, 'learn_logs/index.html')
