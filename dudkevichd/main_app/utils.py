from .models import Post


class MyMixin(object):
    model = Post
    context_object_name = 'posts'
    template_name = 'main_app/category.html'
