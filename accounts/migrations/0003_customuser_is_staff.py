# Generated by Django 5.2.3 on 2025-06-28 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
