# Generated by Django 5.1.5 on 2025-02-03 13:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='عنوان', max_length=200)),
                ('content', models.TextField(help_text='محتوا')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='تاریخ ایجاد')),
                ('image', models.ImageField(help_text='تصویر', upload_to='posts')),
                ('author', models.ForeignKey(help_text='نویسنده', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
