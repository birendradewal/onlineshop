# Generated by Django 3.1.4 on 2021-04-12 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0034_auto_20210411_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitename',
            name='address',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
        migrations.AddField(
            model_name='sitename',
            name='mail',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
    ]
