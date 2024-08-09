from django.contrib import admin
from django.db import models
from django.utils.html import strip_tags

class StripTagsAdminMixin:
    """
    Кастомный класс-миксин для админки Django, который удаляет HTML-теги из текстовых полей перед сохранением.
    """
    def save_model(self, request, obj, form, change):
        for field in obj._meta.fields:
            if isinstance(field, models.TextField):
                value = getattr(obj, field.name)
                if value:
                    setattr(obj, field.name, strip_tags(value))
        super().save_model(request, obj, form, change)