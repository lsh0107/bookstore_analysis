# Generated by Django 3.2.13 on 2022-06-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_remove_platformanalysis_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformanalysis',
            name='aladin',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='platformanalysis',
            name='interpark',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='platformanalysis',
            name='kyobo',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='platformanalysis',
            name='yes',
            field=models.FloatField(null=True),
        ),
    ]
