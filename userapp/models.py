from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    password = models.CharField(max_length=100)
    userName = models.EmailField(max_length=100)
    role = models.CharField(max_length=100)