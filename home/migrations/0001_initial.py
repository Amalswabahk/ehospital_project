# Generated by Django 5.2.1 on 2025-06-04 04:43

import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tagline', models.CharField(blank=True, max_length=300)),
                ('description', models.TextField()),
                ('established_date', models.DateField()),
                ('logo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[200, 200], upload_to='hospital/logo/')),
                ('banner_image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[1200, 400], upload_to='hospital/banner/')),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorHighlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('photo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='doctors/highlights/')),
                ('bio', models.TextField(blank=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='home.hospitalprofile')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentHighlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.CharField(help_text='Font Awesome icon class', max_length=50)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='home.hospitalprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('photo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[100, 100], upload_to='testimonials/')),
                ('rating', models.PositiveSmallIntegerField(default=5)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='home.hospitalprofile')),
            ],
        ),
    ]
