# Generated by Django 5.1.2 on 2024-11-16 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0016_remove_applicationtracking_university_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="applicationtracking",
            old_name="university_model",
            new_name="university",
        ),
    ]
