# Generated by Django 3.0.5 on 2020-05-13 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djaveThread', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loggedcommand',
            old_name='created_at',
            new_name='created',
        ),
    ]
