from django import template
from main_app.models import Post, Tag

register = template.Library()


@register.inclusion_tag('main_app/popular_post.html')
def get_popular_post(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('main_app/tag_cloud.html')
def get_tag_cloud():
    tags = Tag.objects.all()
    return {'tags': tags}
