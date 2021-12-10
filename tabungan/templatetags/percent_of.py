from django import template

register = template.Library()

@register.filter
def percent_of(value, arg):
    return (100 - (((value - sum([x.amount for x in arg]))/value)*100))