# Generated by Django 3.1.6 on 2021-02-22 06:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_thought_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thought',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]