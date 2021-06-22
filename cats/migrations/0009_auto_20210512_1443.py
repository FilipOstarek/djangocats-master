# Generated by Django 3.2 on 2021-05-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0008_remove_description_of_the_cat_fotka'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='fotka',
        ),
        migrations.AddField(
            model_name='description_of_the_cat',
            name='fotka',
            field=models.ImageField(blank=True, null=True, upload_to='cats/fotky/%Y/%m/%d/', verbose_name='Fotka'),
        ),
    ]