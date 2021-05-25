# Generated by Django 3.1.3 on 2021-05-25 10:23

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210420_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to=store.models.content_file_name),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='photo',
            field=models.FileField(upload_to=store.models.content_file_name),
        ),
    ]