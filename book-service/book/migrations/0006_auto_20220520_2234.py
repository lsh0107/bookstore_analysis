# Generated by Django 3.2.13 on 2022-05-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20220520_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='aladin_price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='aladin_review',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='aladin_star',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='avg_star',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='interpark_price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='interpark_review',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='interpark_star',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='kyobo_price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='kyobo_review',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='kyobo_star',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='lowest_price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='yes24_price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='yes24_review',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='yes24_star',
            field=models.CharField(max_length=100),
        ),
    ]
