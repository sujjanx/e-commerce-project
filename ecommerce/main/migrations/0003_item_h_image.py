# Generated by Django 3.0 on 2021-04-03 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210403_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='h_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
