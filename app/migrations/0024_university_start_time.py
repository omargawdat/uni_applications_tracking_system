# Generated by Django 5.1.2 on 2024-11-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0023_university_portal_user_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="university",
            name="start_time",
            field=models.DateField(blank=True, null=True),
        ),
    ]