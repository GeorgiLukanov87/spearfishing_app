from django.template import Library

register = Library()


@register.filter
def placeholder(value, text):
    value.field.widget.attrs['placeholder'] = text
    return value
