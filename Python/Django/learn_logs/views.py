from django.shortcuts import render
from .models import Topic


def index(request):
    """Página Principal do Learn_Log"""
    return render(request, 'learn_logs/index.html')


def topics(request):
    """Mostra Todos os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learn_logs/topics.html', context)


def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'Topic': topic, 'entries': entries}
    return render(request, 'learn_logs/topic.html', context)
