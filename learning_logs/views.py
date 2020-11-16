from django.shortcuts import render
from .models import Topic #import from models.py file

# Create your views here.
# Defined as functions

def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request): #(2) get all topics
    topics = Topic.objects.order_by('date_added')

    context = {'topics':topics} #allows to use template variables

    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id): #integer made in url - get individual topic
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added') # - is decending order

    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context) 


