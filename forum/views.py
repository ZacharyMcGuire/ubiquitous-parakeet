from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Board, Topic, Comment

class IndexView(generic.ListView):
    template_name = 'forum/index.html'

    def get_queryset(self):
        return Board.objects.all()
    
class TopicView(generic.DetailView):
    template_name = 'forum/topic.html'
    model = Topic
    