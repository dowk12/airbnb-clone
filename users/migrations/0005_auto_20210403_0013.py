# Generated by Django 2.2.5 on 2021-04-02 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210402_2358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='langauge',
            new_name='language',
        ),
    ]
