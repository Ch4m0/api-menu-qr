# Generated by Django 3.1.4 on 2020-12-13 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201213_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='photo',
            new_name='foto_producto',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='precio',
        ),
    ]
