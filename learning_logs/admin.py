from django.contrib import admin

# Register your models here.

from .models import Topic #(.) bc it is in the same directory structure
from .models import Entry

admin.site.register(Topic)
admin.site.register(Entry)