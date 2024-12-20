# Generated by Django 4.1.13 on 2024-10-09 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_rename_name_expense_title_alter_expense_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Email_Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(max_length=5000)),
            ],
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.AddField(
            model_name='add_job',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.user'),
        ),
    ]
