# Generated by Django 2.0.1 on 2018-01-14 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20180114_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodimage',
            old_name='title',
            new_name='name',
        ),
    ]
