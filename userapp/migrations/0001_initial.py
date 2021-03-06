# Generated by Django 3.2.12 on 2022-03-30 12:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('profile_image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('password', models.CharField(max_length=100)),
                ('userName', models.EmailField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
    ]
