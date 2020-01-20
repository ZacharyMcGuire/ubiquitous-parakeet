from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Board, Topic, Comment

class IndexView(generic.ListView):
    template_name = 'forum/index.html'

    def get_queryset(self):
        return Board.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topic_list"] = Topic.objects.all()
        return context
    
    