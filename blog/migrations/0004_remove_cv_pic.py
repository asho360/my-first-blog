# Generated by Django 2.2.12 on 2020-08-17 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_cv_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='pic',
        ),
    ]
