from django.shortcuts import render, redirect
from .models import Topic, Entry #import from models.py file
from .forms import TopicForm
from .forms import EntryForm

# Create your views here.
# Defined as functions
# 2

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

#TWO TYPES REQUEST
#GET - get data (loading up with empty fields, no info)
#POST - post data (send info to DB)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else: #request is not blank
        form = TopicForm(data = request.POST) 

        if form.is_valid():#if the form is actually valid
            form.save() #what view will use to take the info and save to DB

            return redirect("learning_logs:topics")

    context= {'form': form}

    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit = False)

            new_entry.topic = topic
            new_entry.save()
            form.save()
            return redirect('learning_logs:topic', topic_id = topic_id)
    
    context = {'form':form, 'topic':topic}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id): #has to match the views.entry
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic #since it is an attribute of entry

    if request.method != 'POST':
        form = EntryForm(instance = entry)
    else:
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
            
    context = {'entry':entry, 'topic':topic, 'form':form} #is a dictionary that is used to pass information to the html
    return render(request, 'learning_logs/edit_entry.html', context)
