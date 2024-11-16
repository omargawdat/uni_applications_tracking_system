# Generated by Django 5.1.2 on 2024-11-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0020_alter_university_options_university_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="applicationtracking",
            name="program_url",
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="applicationtracking",
            name="status",
            field=models.CharField(
                choices=[
                    ("NS", "Not Started"),
                    ("IP", "In Progress"),
                    ("RM", "Requirements Barely Met"),
                    ("AC", "Accepted"),
                    ("RE", "Rejected"),
                ],
                default="NS",
                max_length=2,
            ),
        ),
    ]
