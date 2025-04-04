# Generated by Django 5.1.2 on 2025-01-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0027_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='platform_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='proficiency_1',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='proficiency_2',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='proficiency_3',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='project_1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='project_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='project_3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skill_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skill_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skill_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='status_1',
            field=models.CharField(choices=[('completed', 'Completed'), ('in_progress', 'In Progress'), ('pending', 'Pending')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='status_2',
            field=models.CharField(choices=[('completed', 'Completed'), ('in_progress', 'In Progress'), ('pending', 'Pending')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='status_3',
            field=models.CharField(choices=[('completed', 'Completed'), ('in_progress', 'In Progress'), ('pending', 'Pending')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ProfileLink',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
