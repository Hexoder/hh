# Generated by Django 4.1.3 on 2022-12-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hh', '0007_alter_tagline_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='content',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='smell',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tagline',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
