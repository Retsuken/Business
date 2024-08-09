from django import template
from django.db.models import Q

register = template.Library()

@register.inclusion_tag('article_list.html', takes_context=True)
def show_articles(context, tab_name):
    articles = context['articles'].filter(tip__name=tab_name)
    return {'articles': articles, 'tab_name': tab_name}