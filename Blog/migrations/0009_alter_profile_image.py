# Generated by Django 4.1 on 2022-11-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='static/assets/img/noprofile.jpg', null=True, upload_to='profile/image'),
        ),
    ]
