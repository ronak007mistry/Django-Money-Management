# Generated by Django 3.1.4 on 2020-12-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0008_auto_20201213_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]