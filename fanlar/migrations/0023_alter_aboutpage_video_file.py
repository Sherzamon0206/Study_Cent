# Generated by Django 3.2.4 on 2021-11-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanlar', '0022_auto_20211110_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='video_file',
            field=models.TextField(blank=True, null=True),
        ),
    ]