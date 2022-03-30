# Generated by Django 3.2.12 on 2022-03-30 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Programming and Development', 'Programming and Development'), ('Business', 'Business'), ('Finanance and Accounting', 'Finanance and Accounting'), ('Personal Development', 'Personal Development'), ('Design', 'Design'), ('Lifestyle', 'Lifestyle'), ('Photography and Video', 'Photography and Video'), ('Music', 'Music'), ('Health and Fitness', 'Health and Fitness'), ('Marketing', 'Marketing')], max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='video-content/')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('course_description', models.TextField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnail/course/')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('comments', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_courses', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(related_name='course_categories', to='tutorialapp.Category')),
            ],
        ),
    ]
