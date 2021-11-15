from django import template
from main_app.models import Category

register = template.Library()


@register.inclusion_tag('main_app/menu.html', takes_context=True)
def show_menu(context='context', menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class, 'user': context['user']}
