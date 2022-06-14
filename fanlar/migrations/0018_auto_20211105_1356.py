# Generated by Django 3.2.4 on 2021-11-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanlar', '0017_auto_20211031_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='media/images/')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='media/video/')),
                ('derector_photo', models.ImageField(blank=True, upload_to='media/images/')),
            ],
        ),
        migrations.AlterField(
            model_name='cantact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='fanlar',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
