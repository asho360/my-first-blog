# Generated by Django 2.2.12 on 2020-08-17 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('bio', models.TextField()),
            ],
        ),
    ]
