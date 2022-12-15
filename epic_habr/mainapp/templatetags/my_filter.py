from django import template

register = template.Library()


@register.filter(name='filter')
def function_filter(value, key):
    return value[key]