# Generated by Django 3.1.6 on 2021-02-22 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210220_0040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thought',
            old_name='thought_text',
            new_name='thought',
        ),
        migrations.RenameField(
            model_name='thought',
            old_name='title_text',
            new_name='title',
        ),
    ]
