# Generated by Django 2.0.1 on 2019-03-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0004_auto_20190319_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='skill/photo/media'),
        ),
    ]
