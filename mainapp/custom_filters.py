from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import re
from django.db.models import Q
register = template.Library()

@register.filter(name='remove_tags')
@stringfilter
def remove_tags(value):
    """Удаляет HTML-теги из строки."""
    return re.sub(r'<[^>]*?>', '', value)



