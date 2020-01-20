from django.db import models

class Board(models.Model):
    board_title = models.CharField(max_length=64, null=False, blank=False)
    board_description = models.CharField(max_length=128, null=False, blank=False)
    board_created = models.DateTimeField(verbose_name='date and time the board was created', auto_now_add=True)
    board_modified = models.DateTimeField(verbose_name='date and time the board was most recently modified', auto_now=True)

    def get_topics_in_board(self):
        topics = Topic.objects.filter(board=self)
        return topics

class Topic(models.Model):
    board = models.ForeignKey(to=Board, related_name='topics', on_delete=models.CASCADE)
    topic_title = models.CharField(max_length=64, null=False, blank=False)
    topic_text = models.TextField(max_length=512, null=False, blank=False)
    topic_created = models.DateTimeField(verbose_name='date and time the Topic was created', auto_now_add=True)
    topic_modified = models.DateTimeField(verbose_name='date and time the Topic was most recently modified', auto_now=True)

class Comment(models.Model):
    topic = models.ForeignKey(to=Topic, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=512, null=False, blank=False)
    comment_created = models.DateTimeField(verbose_name='date and time the Comment was created', auto_now_add=True)
    comment_modified = models.DateTimeField(verbose_name='date and time the Comment was most recently modified', auto_now=True)

