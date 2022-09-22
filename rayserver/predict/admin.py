from django.contrib import admin
# Register your models here.
from .models import Post, Test2, Sale, Person
admin.site.register(Post)
admin.site.register(Test2)
admin.site.register(Sale)
admin.site.register(Person)