# Generated by Django 2.0.1 on 2019-03-31 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0011_auto_20190328_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, help_text='50x50px', upload_to='worker/photo'),
        ),
    ]
