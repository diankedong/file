# Generated by Django 2.2.6 on 2019-11-05 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20191105_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='默认图片.png', upload_to='images/'),
        ),
    ]
