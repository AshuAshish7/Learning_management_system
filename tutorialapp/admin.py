from django.contrib import admin

# Register your models here.
from tutorialapp.models import Category, Tutorial, Video, TextContent

admin.site.register((Category, Tutorial, TextContent, Video))
