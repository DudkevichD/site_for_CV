from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Category, Tag, Author, Post, FeedbackModels
from django.utils.safestring import mark_safe


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'file', 'contacts')
    list_display_links = ('title',)
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
    # save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'views', 'category', 'author', 'created_at', 'get_photo')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'tag', 'author')
    search_fields = ('title',)
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'views', 'content', 'tag', 'category', 'author', 'photo', 'get_photo')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" height="40">')
        return '-'

    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(FeedbackModels, FeedbackAdmin)
