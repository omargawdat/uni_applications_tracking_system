# Generated by Django 5.1.2 on 2024-11-16 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0015_rename_website_university_url_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="applicationtracking",
            name="university",
        ),
        migrations.RemoveField(
            model_name="applicationtracking",
            name="url",
        ),
    ]
