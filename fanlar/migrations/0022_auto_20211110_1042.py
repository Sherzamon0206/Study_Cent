# Generated by Django 3.2.4 on 2021-11-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanlar', '0021_auto_20211110_1041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutpage',
            old_name='photo',
            new_name='photo1',
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]
