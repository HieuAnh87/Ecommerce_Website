# Generated by Django 4.1.7 on 2023-02-28 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_alter_vendor_cover_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimages",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="product_images",
                to="core.product",
            ),
        ),
    ]
