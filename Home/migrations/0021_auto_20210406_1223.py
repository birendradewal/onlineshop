# Generated by Django 3.1.6 on 2021-04-06 06:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0020_auto_20210406_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='trending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Coat', 'Coat'), ('Pant', 'Pant'), ('Inner-Coat', 'Inner-Coat'), ('Shirt', 'Shirt'), ('Tie', 'Tie'), ('Daura-Suruwal', 'Daura-Surwal'), ('Dhaka-Topi', 'Dhaka-Topi')], max_length=50)),
                ('added', models.DateTimeField(default=datetime.datetime(2021, 4, 6, 6, 38, 16, 855601, tzinfo=utc))),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='trendingSlide',
        ),
        migrations.AlterField(
            model_name='item',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 6, 38, 16, 845656, tzinfo=utc)),
        ),
    ]
