# Generated by Django 3.2.8 on 2021-11-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='fullname', max_length=255),
        ),
    ]