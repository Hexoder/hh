# Generated by Django 4.1.3 on 2022-12-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hh', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='notes',
            new_name='note1',
        ),
        migrations.AddField(
            model_name='product',
            name='note2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='note3',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]