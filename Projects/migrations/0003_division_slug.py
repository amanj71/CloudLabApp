# Generated by Django 4.2.5 on 2024-03-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0002_project_slug_alter_division_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='slug',
            field=models.SlugField(default='-'),
        ),
    ]