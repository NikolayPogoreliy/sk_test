# Generated by Django 3.1.7 on 2021-03-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('template', '0004_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='filter',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
