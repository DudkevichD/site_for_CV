from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Author(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('author', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='posts', verbose_name='Автор')
    tag = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Теги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-category']

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})


def my_validator(self):
    limit = 1024 * 1024 * 10
    if self.size > limit:
        raise ValidationError('Файл свыше 10MB недопустим')
    self = str(self)
    if self.split('.')[-1] not in ['pdf', 'jpg']:
        raise ValidationError(r'Файл не формата "pdf" или "jpg"')


class FeedbackModels(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название компании")
    content = models.TextField(blank=True, verbose_name='Контент')
    file = models.FileField(upload_to='fail/%Y/%m/%d', blank=True, verbose_name='Файл', validators=[my_validator])
    contacts = models.TextField(blank=True, verbose_name='Контакты')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Приглашение'
        verbose_name_plural = 'Приглашения'
        ordering = ['-created_at']
