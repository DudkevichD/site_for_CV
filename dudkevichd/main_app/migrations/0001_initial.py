# Generated by Django 3.2.9 on 2021-11-04 15:09

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
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
                ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['title'],
                },
            ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
                ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
                },
            ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
                ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['title'],
                },
            ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Опубликовано')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('views', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='main_app.author',
                    verbose_name='Автор'
                    )),
                ('category', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='main_app.category',
                    verbose_name='Категория'
                    )),
                (
                    'tag',
                    models.ManyToManyField(blank=True, related_name='tag', to='main_app.Tag', verbose_name='posts')),
                ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['category'],
                },
            ),
        ]
