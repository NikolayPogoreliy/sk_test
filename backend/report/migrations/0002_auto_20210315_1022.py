# Generated by Django 3.1.7 on 2021-03-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='account',
        ),
        migrations.AddField(
            model_name='report',
            name='account_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='account_name',
            field=models.CharField(default='default', max_length=300),
            preserve_default=False,
        ),
    ]
