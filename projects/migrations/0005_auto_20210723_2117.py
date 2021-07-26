# Generated by Django 3.2.5 on 2021-07-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20210722_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='url',
            new_name='site_url',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='website_url',
        ),
        migrations.RemoveField(
            model_name='project',
            name='github_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='rate',
            name='total_score',
            field=models.FloatField(default=0, null=True),
        ),
    ]
