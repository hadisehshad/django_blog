# Generated by Django 5.1.5 on 2025-02-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(help_text='تصویر', upload_to='posts/'),
        ),
    ]
