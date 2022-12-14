# Generated by Django 3.2.8 on 2022-12-14 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активен')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название статьи')),
                ('posted_at', models.DateTimeField(blank=True, verbose_name='Дата публикации')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(max_length=32, verbose_name='Тема статьи')),
                ('text', models.TextField(blank=True, verbose_name='Статья')),
                ('is_posted', models.BooleanField(default=False, verbose_name='размещена')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.author')),
            ],
        ),
    ]
