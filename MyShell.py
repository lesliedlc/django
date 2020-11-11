import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from learning_logs.models import Topic

##1
topics = Topic.objects.all() #Similar to select * 

for topic in topics:
    print('Topic ID:', topic.id, 'Topic:', topic) #no need to put .text bc the string method is defined in models

##2
# knowing the id
t = Topic.objects.get(id = 1)
print(t.text)
print(t.date_added)

##3
entries = t.entry_set.all() #lowercase model_set.all will bring all related entries for specific topic

for entry in entries: #acess each entry related to topic
    print(entry) #.text will override the string defined and print out all text