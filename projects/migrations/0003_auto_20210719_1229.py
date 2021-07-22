# Generated by Django 3.2.5 on 2021-07-19 12:29

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_alter_project_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='rating',
        ),
        migrations.AddField(
            model_name='project',
            name='content',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='design',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=url_or_relative_url_field.fields.URLOrRelativeURLField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/playboard/image/upload/v1626529829/vjytnast5wblft8xvy9p.jpg', max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=url_or_relative_url_field.fields.URLOrRelativeURLField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='usability',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='details',
            field=tinymce.models.HTMLField(),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', tinymce.models.HTMLField(max_length=100)),
                ('profile_pic', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/playboard/image/upload/v1626529829/vjytnast5wblft8xvy9p.jpg', max_length=255)),
                ('website_url', url_or_relative_url_field.fields.URLOrRelativeURLField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]