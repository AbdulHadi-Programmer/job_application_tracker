# Generated by Django 4.1.13 on 2024-10-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0016_add_job_company_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_job',
            name='company_email',
            field=models.EmailField(blank=True, max_length=150, null=True),
        ),
    ]
