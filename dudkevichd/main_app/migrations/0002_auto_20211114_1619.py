# Generated by Django 3.2.9 on 2021-11-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название компании')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('file', models.FileField(blank=True, upload_to='fail/%Y/%m/%d', verbose_name='Файл')),
                ('contacts', models.TextField(blank=True, verbose_name='Контакты')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name': 'Приглашение',
                'verbose_name_plural': 'Приглашения',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-category'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='posts', to='main_app.Tag', verbose_name='Теги'),
        ),
    ]