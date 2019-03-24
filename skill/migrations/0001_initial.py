# Generated by Django 2.0.1 on 2019-03-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=200)),
                ('body', models.TextField(max_length=400)),
            ],
        ),
    ]
