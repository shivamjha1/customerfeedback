# Generated by Django 5.0.2 on 2024-04-15 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_review_review_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='oneword_review',
            field=models.CharField(default='Good', max_length=20),
        ),
    ]