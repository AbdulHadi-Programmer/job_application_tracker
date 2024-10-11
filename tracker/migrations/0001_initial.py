# Generated by Django 4.1.13 on 2024-10-04 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_category', models.CharField(max_length=100)),
                ('job_level', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('reference_link', models.URLField()),
                ('employment_type', models.CharField(max_length=100)),
            ],
        ),
    ]