# Generated by Django 3.2.23 on 2023-11-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_sample_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='name',
        ),
        migrations.AddField(
            model_name='sample',
            name='attachment',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]