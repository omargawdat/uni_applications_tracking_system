# Generated by Django 5.1.2 on 2024-11-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_alter_applicationtracking_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="applicationtracking",
            old_name="program",
            new_name="university",
        ),
        migrations.AddField(
            model_name="applicationtracking",
            name="url",
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="applicationtracking",
            name="field",
            field=models.CharField(
                choices=[
                    ("AI", "Artificial Intelligence"),
                    ("CS", "Computer Science"),
                    ("CYB", "Cyber Security"),
                    ("DS", "Data Science"),
                ],
                help_text="Main field of study",
                max_length=3,
                null=True,
            ),
        ),
    ]
