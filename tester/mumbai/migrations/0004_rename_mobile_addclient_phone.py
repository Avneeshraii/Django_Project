# Generated by Django 4.2.5 on 2023-09-29 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mumbai', '0003_rename_client_addclient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addclient',
            old_name='mobile',
            new_name='phone',
        ),
    ]