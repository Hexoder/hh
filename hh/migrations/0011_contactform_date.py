# Generated by Django 4.1.3 on 2022-12-11 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hh', '0010_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
