from django import template
register = template.Library()

@register.filter
def substracted_by(value, arg):
    return value - arg