from django.contrib import admin

from .models import Board, Topic, Comment

admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Comment)