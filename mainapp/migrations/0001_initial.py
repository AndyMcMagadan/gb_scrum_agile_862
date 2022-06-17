# Generated by Django 3.2.13 on 2022-06-17 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HabrCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Категория')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('category_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Habr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, upload_to='article_images')),
                ('short_desc', models.CharField(blank=True, max_length=256, verbose_name='Аннотация')),
                ('description', models.TextField(blank=True, verbose_name='Содержание')),
                ('article_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.habrcategory')),
            ],
        ),
    ]
