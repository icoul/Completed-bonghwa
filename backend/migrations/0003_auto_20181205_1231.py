# Generated by Django 2.0.5 on 2018-12-05 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20181125_0507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contents',
            old_name='created_date',
            new_name='createdDate',
        ),
        migrations.RenameField(
            model_name='contents',
            old_name='mention_order',
            new_name='mentionDepth',
        ),
        migrations.RenameField(
            model_name='contents',
            old_name='mention_index',
            new_name='mentionIndex',
        ),
    ]