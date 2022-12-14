# Generated by Django 4.1 on 2022-11-08 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_category_article_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('title', models.CharField(max_length=85)),
                ('body', models.TextField(max_length=750)),
            ],
        ),
    ]
