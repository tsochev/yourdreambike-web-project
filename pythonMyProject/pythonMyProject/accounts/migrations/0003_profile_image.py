# Generated by Django 4.0.3 on 2022-04-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_appuser_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1, upload_to='mediafiles'),
            preserve_default=False,
        ),
    ]