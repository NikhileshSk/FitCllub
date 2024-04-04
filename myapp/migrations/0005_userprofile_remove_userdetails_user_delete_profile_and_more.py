# Generated by Django 4.2.2 on 2023-10-03 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0004_alter_profile_is_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]