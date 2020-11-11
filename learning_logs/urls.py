from django.urls import path
from . import views

app_name = 'learning_logs'

#'' null is the homepage
## 1 set up URL
urlpatterns = [
    path('', views.index, name = 'index'),
    path('', views.topics, name = 'topics') ##exercise
]