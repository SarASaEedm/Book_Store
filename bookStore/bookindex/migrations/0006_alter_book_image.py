# Generated by Django 5.0.4 on 2024-04-29 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookindex', '0005_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bookindex/images/'),
        ),
    ]
