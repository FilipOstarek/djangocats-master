# Generated by Django 3.2 on 2021-05-11 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_description_of_the_cat_fotky'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='fotka',
            field=models.ImageField(blank=True, null=True, upload_to='cats/fotky/%Y/%m/%d/', verbose_name='Fotka'),
        ),
    ]