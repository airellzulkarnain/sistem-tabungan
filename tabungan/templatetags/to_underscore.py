from django import template

register = template.Library()

@register.filter
def  to_underscore(value):
    return value.replace(" ", "_")