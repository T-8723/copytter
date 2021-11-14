from django.contrib import admin
from .models import Follow, Entry, Profile

# Register your models here.

admin.site.register(Entry)
admin.site.register(Follow)
admin.site.register(Profile)
