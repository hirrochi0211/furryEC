# Generated by Django 2.2 on 2021-10-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create_Time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Update_Time')),
                ('is_delete', models.BooleanField(default=False, verbose_name='DeleteOrNot')),
                ('is_show', models.BooleanField(default=False, verbose_name='DisplayOrNot')),
                ('display_order', models.IntegerField()),
                ('name', models.CharField(max_length=32, verbose_name='img_name')),
                ('img', models.ImageField(help_text='The size must be 3840*800', null=True, upload_to='banner', verbose_name='Carousel img')),
                ('link', models.CharField(max_length=32, verbose_name='the Link to another url')),
                ('info', models.TextField(verbose_name='img_description')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
