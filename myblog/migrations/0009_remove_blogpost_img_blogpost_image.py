# Generated by Django 4.0 on 2022-03-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_alter_blogpost_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='img',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(null=True, upload_to='myimg/%y/%m/%d/'),
        ),
    ]