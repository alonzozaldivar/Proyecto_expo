# Generated by Django 4.2.7 on 2023-11-28 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_slug_bano_codigo_rename_slug_cocina_codigo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bano',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='cocina',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='comedor',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='oficina',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='recamara',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='sala',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]