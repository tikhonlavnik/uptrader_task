from django import template
from menu.models import *


register = template.Library()


@register.inclusion_tag('menu/create_menu.html')
def draw_menu(slug, chosen_item=None):
    """Chosen_item нужен для подсветки выбранного элемента"""
    menu = Menu.objects.filter(slug=slug)
    return {'menu': menu, 'chosen_item': chosen_item}

# <!--        {% if menu_item.subcategory_id == chosen_item.id or menu_menu_item.id < menu_menu_item.subcategory_id %}-->
