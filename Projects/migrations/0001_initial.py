# Generated by Django 4.2.4 on 2023-12-06 07:10

import Projects.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['division'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_company', models.CharField(default='BPI', max_length=255)),
                ('project', models.CharField(max_length=255)),
                ('client', models.CharField(blank=True, max_length=255)),
                ('project_location_name', models.CharField(blank=True, max_length=255)),
                ('geometry_nodes', models.FloatField(blank=True, null=True)),
                ('project_description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('depth_from', models.FloatField()),
                ('depth_to', models.FloatField(validators=[Projects.models.validate_depth])),
                ('sample_type', models.CharField(choices=[('Bag', 'Bag'), ('SPT', 'SPT'), ('Shelby', 'Shelby')], default='Bag', max_length=8)),
                ('sample_description', models.TextField(blank=True)),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='division_related', to='Projects.division')),
            ],
        ),
        migrations.CreateModel(
            name='BoreHole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borehole', models.CharField(blank=True, max_length=255, null=True)),
                ('depth', models.FloatField(null=True)),
                ('receive_date', models.DateField(null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='project_related', to='Projects.project')),
            ],
        ),
    ]
