# Generated by Django 5.2.3 on 2025-06-28 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='app_icons/'),
        ),
        migrations.AddField(
            model_name='app',
            name='link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='sub_category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
