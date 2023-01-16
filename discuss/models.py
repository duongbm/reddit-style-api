from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=True)
    modified_date = models.DateTimeField(auto_now=True)


class Discuss(Base):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(Base):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='commentator')
    discussion = models.ForeignKey(Discuss, on_delete=models.CASCADE, related_name='comment', name='discussion_id')
    parent = models.ForeignKey("self", blank=True, null=True, related_name='parent_comment', on_delete=models.CASCADE)
    content = models.TextField()
