# Generated by Django 4.0 on 2022-03-11 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_alter_blogpost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/%y'),
        ),
    ]