from django.contrib import admin

# Register your models here.
from .models import Writing, Post1, Comment

admin.site.register(Writing)
admin.site.register(Post1)
admin.site.register(Comment)