# Generated by Django 3.1.8 on 2021-04-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='address',
            field=models.CharField(default='thane', max_length=50),
        ),
        migrations.AddField(
            model_name='demo',
            name='marks',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='demo',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
