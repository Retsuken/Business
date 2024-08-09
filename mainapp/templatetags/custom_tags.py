from django import template

register = template.Library()

@register.filter
def add_to_list(value, arg):
    value.append(arg)
    return value