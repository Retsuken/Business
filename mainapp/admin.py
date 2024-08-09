from django.contrib import admin
from .models import program_teacher, Reviews, service, service_faq, Person, articles_inner, Cases, About, Activities, Teg, tip_news, FilterArticle, Otrasl, StatusArticle, GroupSpec, document, Program, Format, Partners, Program_sod, Obuch, Obuch_Desc, Collections_watches, Personteg, TegiNews, News, Form_Home
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
class MyModelAdmin(admin.ModelAdmin):
   
    readonly_fields = ('display_admin_image',)
    def display_admin_image(self, obj):
        return format_html('<img src="{}" width="150" height="150" />', obj.image.url)

    display_admin_image.short_description = 'Изображение'
  

admin.site.register(program_teacher, MyModelAdmin)

admin.site.register(Collections_watches)

class MyModelAdmin3(SummernoteModelAdmin):
    summernote_fields = ('field_activity', 'professional_experience', 'education', 'dop_education', 'students_disciplined', 'membership_editorial_boards', 'publications_appearances')
    readonly_fields = ('display_admin_image',)
    def display_admin_image(self, obj):
        return format_html('<img src="{}" width="150" height="150" />', obj.image.url)

    display_admin_image.short_description = 'Изображение'
  

admin.site.register(Person, MyModelAdmin3)

class MyModelAdmin4(SummernoteModelAdmin):
   
    readonly_fields = ('display_admin_image',)
    summernote_fields = ('description')
    def display_admin_image(self, obj):
        return format_html('<img src="{}" width="150" height="150" />', obj.image.url)

    display_admin_image.short_description = 'Изображение'
  

admin.site.register(articles_inner, MyModelAdmin4)


class MyModelAdmin111(SummernoteModelAdmin):
    summernote_fields = ('description')

admin.site.register(Form_Home, MyModelAdmin111)



class MyModelAdmin26(SummernoteModelAdmin):
    summernote_fields = ('description')

admin.site.register(News, MyModelAdmin26)
class MyModelAdmin6(admin.ModelAdmin):
   
    readonly_fields = ('display_admin_image',)
    def display_admin_image(self, obj):
        return format_html('<img src="{}" width="150" height="150" />', obj.image.url)

    display_admin_image.short_description = 'Изображение'
  

admin.site.register(Cases, MyModelAdmin6)


class MyModelAdmin8(admin.ModelAdmin):
   
    readonly_fields = ('display_admin_image',)
    def display_admin_image(self, obj):
        return format_html('<img src="{}" width="150" height="150" />', obj.image.url)

    display_admin_image.short_description = 'Изображение'
  

admin.site.register(About, MyModelAdmin8)

class MyModelAdmin9(admin.ModelAdmin):
   
    readonly_fields = ('display_admin_image',)
    def display_admin_image(self, obj):
        return format_html('<img src="{}" width="150" height="150" />', obj.image.url)

    display_admin_image.short_description = 'Изображение'
  


class MyModelAdmin20(admin.ModelAdmin):
   
    readonly_fields = ('display_admin_image',)
    def display_admin_image(self, obj):
        return format_html('<img src="{}" width="150" height="150" />', obj.image.url)

    display_admin_image.short_description = 'Изображение'
  

admin.site.register(Partners, MyModelAdmin20)

admin.site.register(Activities, MyModelAdmin9)
admin.site.register(tip_news)
admin.site.register(Teg)
admin.site.register(Reviews)
admin.site.register(service)
admin.site.register(service_faq)
admin.site.register(FilterArticle)
admin.site.register(Otrasl)
admin.site.register(StatusArticle)
admin.site.register(GroupSpec)

admin.site.register(Format)
admin.site.register(Program)
admin.site.register(Program_sod)

admin.site.register(Obuch_Desc)
admin.site.register(Personteg)
admin.site.register(TegiNews)

class Category1Admin(admin.ModelAdmin):
    model = document


class Category2Admin(admin.ModelAdmin):
    model = Obuch


admin.site.register(document, Category1Admin)
admin.site.register(Obuch, Category2Admin)
