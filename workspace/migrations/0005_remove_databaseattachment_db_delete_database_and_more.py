# Generated by Django 5.0.2 on 2024-04-15 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0004_alter_database_workspace'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='databaseattachment',
            name='db',
        ),
        migrations.DeleteModel(
            name='Database',
        ),
        migrations.DeleteModel(
            name='DatabaseAttachment',
        ),
    ]
