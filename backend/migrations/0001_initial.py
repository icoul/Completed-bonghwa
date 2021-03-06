# Generated by Django 2.0.5 on 2018-11-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mention_index', models.CharField(default='0', max_length=5)),
                ('mention_order', models.CharField(default='0', max_length=5)),
                ('username', models.CharField(max_length=40)),
                ('contents', models.CharField(max_length=150)),
                ('image', models.FileField(null=True, upload_to='')),
                ('created_date', models.CharField(max_length=20)),
                ('dm', models.IntegerField(default=0)),
                ('deleted', models.IntegerField(default=0)),
            ],
        ),
    ]
