# Generated by Django 4.0.5 on 2022-07-14 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App19', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(default='exit', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='email',
            field=models.EmailField(default='tettymartinez95@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='profesion',
            field=models.CharField(default='profesor', max_length=40),
            preserve_default=False,
        ),
    ]