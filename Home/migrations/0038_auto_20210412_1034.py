# Generated by Django 3.1.4 on 2021-04-12 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0037_auto_20210412_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitename',
            name='address',
            field=models.TextField(),
        ),
    ]
