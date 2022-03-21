from django.contrib import admin
from .models import Profile, Gender, Post, Hood, Business, PostType

# Register your models here.
admin.site.register(Profile)
admin.site.register(Gender)
admin.site.register(Post)
admin.site.register(Hood)
admin.site.register(Business)
admin.site.register(PostType)
