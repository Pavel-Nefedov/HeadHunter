from django import template

register = template.Library()


@register.filter(name='get_from_dict')
def function_filter(my_dict, key):
    return my_dict.get(key)


@register.filter(name='path_contain')
def function_filter(path, controller):
    return controller in path
