from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('topic/<int:pk>', views.TopicView.as_view(), name='topic'),
]