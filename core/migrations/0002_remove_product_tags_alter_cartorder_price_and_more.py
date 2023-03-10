# Generated by Django 4.1.7 on 2023-02-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='price',
            field=models.DecimalField(decimal_places=2, default='1.99', max_digits=999999999999),
        ),
        migrations.AlterField(
            model_name='cartorderitems',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=999999999999),
        ),
        migrations.AlterField(
            model_name='cartorderitems',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=999999999999),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default='1.99', max_digits=999999999999),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='1.99', max_digits=99999999999999),
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
