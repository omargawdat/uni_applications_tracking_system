# Generated by Django 5.1.2 on 2024-11-23 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0030_alter_applicationtracking_field"),
    ]

    operations = [
        migrations.RenameField(
            model_name="applicationtracking",
            old_name="application_submission_date",
            new_name="start_date",
        ),
    ]