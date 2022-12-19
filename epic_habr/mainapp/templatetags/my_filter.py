from django import template

from common.utils import from_cyrillic_to_eng

register = template.Library()


@register.filter(name='get_from_dict')
def function_filter(my_dict, key):
    return my_dict.get(key)


@register.filter(name='path_contain')
def function_filter(path, controller):
    return controller in path

@register.filter(name='from_cyrillic_to_eng')
def function_filter(cyr_name):
    return from_cyrillic_to_eng(cyr_name)




