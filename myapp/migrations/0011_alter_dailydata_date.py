# Generated by Django 5.0.1 on 2024-01-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_modulecompletion_completed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailydata',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]