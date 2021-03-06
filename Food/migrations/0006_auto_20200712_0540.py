# Generated by Django 3.0.5 on 2020-07-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0005_auto_20200711_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_desc',
            field=models.CharField(max_length=200, verbose_name='Item Discription'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://image.flaticon.com/icons/svg/1344/1344788.svg', max_length=200, verbose_name='Item Image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=200, verbose_name='Item Name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_price',
            field=models.IntegerField(verbose_name='Item Price'),
        ),
    ]
