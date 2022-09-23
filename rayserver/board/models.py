from tkinter import CASCADE
from django.db import models
from member.models import Members

# Create your models here.
class Writing(models.Model):
    mem_id = models.ForeignKey(Members, on_delete=models.CASCADE, null=False)
    subject = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'test33'
        verbose_name = '테스트33'

    def __str__(self):
        return self.subject

    
class Writing2(models.Model):
    mem_id = models.ForeignKey(Members, on_delete=models.CASCADE, null=False)
    subject = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'writing2'
        verbose_name = 'writing2'

    def __str__(self):
        return self.subject


# Create your models here.
class Post1(models.Model):
    id = models.BigAutoField(help_text="Post ID", primary_key=True)
    title = models.CharField(help_text="Post title", max_length=100, blank=False, null=False)
    contents = models.TextField(help_text="post contents", blank=False, null=False)


class Comment(models.Model):
    id = models.BigAutoField(help_text="Comment ID", primary_key=True)
    post_id = models.ForeignKey("Post1", related_name="post", on_delete=models.CASCADE, db_column="post_id")
    contents = models.TextField(help_text="Comment contents", blank=False, null=False)