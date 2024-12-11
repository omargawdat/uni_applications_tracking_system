# Generated by Django 5.1.2 on 2024-12-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0037_alter_applicationtracking_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicationtracking",
            name="status",
            field=models.CharField(
                choices=[
                    ("NS", "Not Started"),
                    ("IP", "In Progress"),
                    ("HA", "Hard Application"),
                    ("WO", "Waiting for Opening"),
                    ("AC", "Accepted"),
                    ("RE", "Rejected"),
                ],
                default="NS",
                max_length=2,
            ),
        ),
    ]
