from django.db import models

# Create your models here.
# Create model of database

class Topic(models.Model):
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)


    def __str__(self): #returns the text related to the text field
        return self.text 


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE) 
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta: #does entry as plural to be correct in the site
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."