# Generated by Django 3.2.13 on 2022-06-07 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_remove_bestseller_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformanalysis',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
