# Generated by Django 4.1.13 on 2024-10-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0017_alter_add_job_company_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.CharField(choices=[('5', '⭐⭐⭐⭐⭐ - Excellent'), ('4', '⭐⭐⭐⭐ - Good'), ('3', '⭐⭐⭐ - Average'), ('2', '⭐⭐ - Poor'), ('1', '⭐ - Terrible')], default='----------', max_length=10),
        ),
    ]
