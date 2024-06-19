# Generated by Django 4.2.5 on 2024-03-29 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0007_alter_sample_random_string'),
        ('WaterContent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watercontent',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.sample'),
        ),
        migrations.AlterUniqueTogether(
            name='watercontent',
            unique_together={('project', 'division')},
        ),
    ]