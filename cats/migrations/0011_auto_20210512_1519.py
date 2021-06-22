# Generated by Django 3.2 on 2021-05-12 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0010_auto_20210512_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description_of_the_cat',
            name='fotky',
        ),
        migrations.AddField(
            model_name='photo',
            name='fotka',
            field=models.ImageField(blank=True, null=True, upload_to='cats/fotky/%Y/%m/%d/', verbose_name='Fotka'),
        ),
        migrations.AlterField(
            model_name='description_of_the_cat',
            name='fotka',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cats.photo'),
            preserve_default=False,
        ),
    ]