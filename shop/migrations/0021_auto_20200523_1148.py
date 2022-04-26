# Generated by Django 3.0.6 on 2020-05-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20200523_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='contact',
            field=models.CharField(default='123456789', max_length=15),
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(default='Nepal', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.CharField(default='Sajilobook', max_length=50),
        ),
    ]