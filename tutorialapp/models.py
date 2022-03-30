from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
import uuid

USER = settings.AUTH_USER_MODEL


class Category(models.Model):
    categories = [
        ('Programming and Development', 'Programming and Development'), ('Business',
                                                                         'Business'), ('Finanance and Accounting', 'Finanance and Accounting'),
        ('Personal Development', 'Personal Development'), ('Design', 'Design'), ('Lifestyle',
                                                                                 'Lifestyle'), ('Photography and Video', 'Photography and Video'),
        ('Music', 'Music'), ('Health and Fitness', 'Health and Fitness'), ('Marketing', 'Marketing')
    ]
    name = models.CharField(max_length=100, choices=categories, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Tutorial(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    author = models.ForeignKey(USER, on_delete=models.PROTECT, related_name='created_courses')
    # remove null = True
    categories = models.ManyToManyField(
        Category, related_name="course_categories")
    title = models.CharField(max_length=500)
    description = models.TextField()
    course_description = models.TextField()
    # not meant to be nullable. change it
    thumbnail = models.ImageField(upload_to='thumbnail/course/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    comments = models.TextField()

    def __str__(self):
        return self.name


class Video(models.Model):
    url = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='video-content/', blank=True, null=True)

class TextContent(models.Model):
    content = models.TextField()