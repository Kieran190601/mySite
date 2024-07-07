from django.contrib import admin
from .models import BlogPost, Question, Choice

admin.site.register(BlogPost)
admin.site.register(Question)
admin.site.register(Choice)
