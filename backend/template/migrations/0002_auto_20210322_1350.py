# Generated by Django 3.1.7 on 2021-03-22 13:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('template', '0001_initial'),
    ]

    operations = [
        # migrations.RenameField(
        #     model_name='chart',
        #     old_name='dimension',
        #     new_name='dimensions',
        # ),
        migrations.RenameField(
            model_name='chart',
            old_name='pivot',
            new_name='pivots',
        ),
        # migrations.RenameField(
        #     model_name='pivot',
        #     old_name='dimension',
        #     new_name='dimensions',
        # ),
    ]
