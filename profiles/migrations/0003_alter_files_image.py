# Generated by Django 5.0.2 on 2024-04-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_files_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='image',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
