# Generated by Django 5.1.2 on 2024-10-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_universityprogram_application_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_available', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='applicationtracking',
            name='decision_date',
        ),
        migrations.AddField(
            model_name='applicationtracking',
            name='end_date',
            field=models.DateField(blank=True, help_text='Application end date', null=True),
        ),
        migrations.AddField(
            model_name='applicationtracking',
            name='start_date',
            field=models.DateField(blank=True, help_text='Application start date', null=True),
        ),
        migrations.AddField(
            model_name='applicationtracking',
            name='required_docs',
            field=models.ManyToManyField(blank=True, related_name='required_in_applications', to='app.document'),
        ),
    ]
