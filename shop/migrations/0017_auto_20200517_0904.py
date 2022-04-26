# Generated by Django 3.0.6 on 2020-05-17 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20200517_0656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_code',
            new_name='slug',
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('title', 'slug')},
        ),
    ]
