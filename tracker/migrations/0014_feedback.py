# Generated by Django 4.1.13 on 2024-10-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0013_alter_add_job_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('rating', models.CharField(choices=[(5, '⭐⭐⭐⭐⭐ - Excellent'), (4, '⭐⭐⭐⭐ - Good'), (3, '⭐⭐⭐ - Average'), (2, '⭐⭐ - Poor'), (1, '⭐ - Terrible')], max_length=10)),
                ('feedback_box', models.TextField(max_length=5000)),
            ],
        ),
    ]
