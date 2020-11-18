from django.urls import path
from . import views

app_name = 'learning_logs'

#'' null is the homepage
## 1 set up URL
urlpatterns = [
    path('', views.index, name = 'index'), #'' is the homepage
    path('topics', views.topics, name = 'topics'), #this would be homepage/topics/html (1)
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    path('new_topic/', views.new_topic, name = 'new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
]