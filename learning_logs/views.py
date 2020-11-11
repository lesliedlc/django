from django.shortcuts import render

# Create your views here.
# Defined as functions

def index(request):
    return render(request, 'learning_logs/index.html')

##exercise, aside from topics.html and base.html edits
def topics(request):
    return render(request, 'learning_logs/topics.html')
