from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from datetime import datetime
from transliterate import translit





class Format(models.Model):
    FormatProgramm = models.TextField()
    def __str__(self):
        return self.FormatProgramm
    
    class Meta:
        verbose_name = 'Формат обучение'
        verbose_name_plural = 'Формат обучение'


class document(models.Model):
    Document = models.TextField()

    def __str__(self):
        return self.Document
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документ'


class Program_sod(models.Model):
    sod = models.TextField(_("Содержание"))
     
    def __str__(self):
        return self.sod
    
    class Meta:
        verbose_name = 'Содержание программы'
        verbose_name_plural = 'Содержание программы'


class Obuch(models.Model):
    obuch = models.TextField(_("Заголовок"))

     
    def __str__(self):
        return self.obuch
    
    class Meta:
        verbose_name = 'Кому подойдет обучение Заголовок'
        verbose_name_plural = 'Кому подойдет обучение Заголовок'

class Obuch_Desc(models.Model):
    obuch_desc = models.TextField(_("Описание"))

    def __str__(self):
        return self.obuch_desc

    class Meta:
        verbose_name = 'Кому подойдет обучение Описание'
        verbose_name_plural = 'Кому подойдет обучение Описание'

class Program(models.Model):
    name = models.CharField(_("Название программы"), max_length=128)
    description = models.TextField(_("Описание программы"))
    price = models.IntegerField(_("Стоимость программы"))
    date = models.DateField(_("Дата старта курса"), default=datetime.now)
    prod = models.IntegerField(_("Продолжительность программы"))
    prod_mes = models.CharField(_("Продолжительность программы в месяцах"), null=True, blank=True, max_length=128)
    formats = models.ForeignKey(to=Format, on_delete=models.CASCADE)
    documents = models.ForeignKey(to=document, on_delete=models.CASCADE)
    rejim = models.CharField(_("Режим занятий"), max_length=128)
    zagolovok_kras = models.CharField(_("Заголовок красным"), max_length=128)
    zagolovok = models.CharField(_("Заголовок - продолжение"), max_length=128)
    pred_nav = models.TextField(_("Приобретаемый навык"))
    vhod = models.TextField(_("В стоймость входит"))
    desc = models.TextField(_("Стоймость обучение описание"))
    sale = models.IntegerField(_("Размер скидки (%)"), null=True, blank=True)
    rasroch = models.BooleanField(_("Рассрочка"))
    rasroch_mes = models.TextField(_("В месяц по рассрочке"), null=True, blank=True)
    ot = models.IntegerField(_("Сумма рассрочки в месяц"), null=True, blank=True)
    skidka_do = models.DateField(_("Дата завершения акции"), null=True, blank=True)
    program_soderj = models.ManyToManyField(Program_sod, verbose_name='Программа (содержание)')
    komu_obuch_zagolovok = models.ManyToManyField(Obuch, verbose_name='Кому обучение (заголовок)')
    komu_obuch_description = models.ManyToManyField(Obuch_Desc, verbose_name='Кому обучение (описание)')
    image = models.ImageField(_("Логотипы"), null=True, blank=True,  upload_to='logo_image')
    Meta_Description = models.CharField(_("Описание (мета тег)"), max_length=156)
    program_url = models.CharField(_("URL сервиса"), max_length=256, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        # Создание уникального URL из поля name_service с транслитерацией русских символов
        if not self.program_url:
            name_translit = translit(self.name, 'ru', reversed=True)
            self.program_url = slugify(name_translit)
        super().save(*args, **kwargs)



    def __str__(self):
        return self.name






    class Meta:
        verbose_name = 'Программы'
        verbose_name_plural = 'Программы'

class program_teacher(models.Model):
    name = models.CharField(_("Имя"), max_length=128)
    profession = models.CharField(_("Профессия"), max_length=128)
    description = models.TextField(_("Описание"))
    image = models.ImageField(_("Сменить изображение"), upload_to='profession_images')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Преподаватели'
        verbose_name_plural = 'Преподаватели' 



class Reviews(models.Model):
    description = models.TextField(_("Описание")) 
    author = models.CharField(_("Автор"), max_length=64)

    def __str__(self):
        return self.author    
    
    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

class Collections_watches(models.Model):
    kolection = models.TextField(_("Категория (сервисы)"))


    def __str__(self):
        return self.kolection
    
    class Meta:
        verbose_name = 'Категория (сервисы)'
        verbose_name_plural = 'Категория (сервисы)'
    
class service(models.Model):
    name_service = models.CharField(_("Название сервиса"), max_length=156)
    description = models.TextField(_("Описание"))
    name = models.TextField(_("Имя"))
    Meta_Description = models.CharField(_("Описание (мета тег)"), max_length=156)
    collections = models.ForeignKey(Collections_watches, on_delete=models.CASCADE, verbose_name='Категория' ,blank=True,null=True,related_name='watches_collections')
    service_url = models.CharField(_("URL сервиса"), max_length=256, blank=True, null=True, unique=True)
    
    def __str__(self):
        return self.name_service  


    def save(self, *args, **kwargs):
        # Создание уникального URL из поля name_service с транслитерацией русских символов
        if not self.service_url:
            name_translit = translit(self.name_service, 'ru', reversed=True)
            self.service_url = slugify(name_translit)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Сервисы'
        verbose_name_plural = 'Сервисы'

class service_faq(models.Model):
    name = models.CharField(_("Имя"), max_length=128)
    description = models.TextField(_("Описание"))

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Сервисы FAQ'
        verbose_name_plural = 'Сервисы FAQ' 

class Personteg(models.Model):
    tegis = models.TextField(_("Тег (команда)"))
    def __str__(self):
        return self.tegis
    class Meta:
        verbose_name = 'Теги (команда)'
        verbose_name_plural = 'Теги (команда)' 



class Person(models.Model):
    image = models.ImageField(_("Сменить изображение"), upload_to='person_images')
    name = models.CharField(_("Имя"), max_length=156)
    field_activity = models.TextField(_("Сфера научной деятельности"), null=True, blank=True)
    age = models.PositiveIntegerField(_("Стаж работы"))
    professional_experience = models.TextField(_("Профессиональный опыт"), null=True, blank=True)
    education = models.TextField(_("Образование"), null=True, blank=True)
    dop_education = models.TextField(_("Дополнительное образование"), null=True, blank=True)
    students_disciplined = models.TextField(_("Преподаваемые дисциплины и курсы"), null=True, blank=True)
    membership_editorial_boards = models.TextField(_("Членство в редколлегиях"), null=True, blank=True)
    publications_appearances = models.TextField(_("Публикации и выступления в СМИ"), null=True, blank=True)
    Meta_Description = models.CharField(_("Описание (мета тег)"), max_length=156)
    person_url = models.CharField(_("URL сервиса"), max_length=256, blank=True, null=True, unique=True)
    tegis = models.ManyToManyField(Personteg, verbose_name='Теги (команда)')
    koord = models.BooleanField(_("Координационный совет"))
    

    def save(self, *args, **kwargs):
        # Создание уникального URL из поля name_service с транслитерацией русских символов
        if not self.person_url:
            name_translit = translit(self.name, 'ru', reversed=True)
            self.person_url = slugify(name_translit)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команда' 



class tip_news(models.Model):
    tip = models.TextField(_("Тип статьи"))
    class Meta:
        verbose_name = 'Тип статьи'
        verbose_name_plural = 'Тип статьи'
    def __str__(self):
        return self.tip
    
class FilterArticle(models.Model):
    filter = models.TextField(_("Фильтр"))

    class Meta:
        verbose_name = 'Фильтры статей'
        verbose_name_plural = 'Фильтры статей'
    def __str__(self):
        return self.filter


class Otrasl(models.Model):
    OtraslNauki = models.TextField()

    class Meta:
        verbose_name = 'Отрасль науки Статьи'
        verbose_name_plural = 'Отрасль науки Статьи'
    def __str__(self):
        return self.OtraslNauki
    
class StatusArticle(models.Model):
    Status = models.TextField()

    class Meta:
        verbose_name = 'Статус для Статей'
        verbose_name_plural = 'Статус для Статей'
    def __str__(self):
        return self.Status
    
class GroupSpec(models.Model):
    GroupSpec = models.TextField(_("Группа специальностей"))

    class Meta:
        verbose_name = 'Группа специальностей для статей'
        verbose_name_plural = 'Группа специальностей для статей'
    def __str__(self):
        return self.GroupSpec

class TegiNews(models.Model):
    teg = models.TextField("Теги")

    class Meta:
        verbose_name = 'Теги (статьи)'
        verbose_name_plural = 'Теги (статьи)'
    def __str__(self):
        return self.teg

class News(models.Model):
    articles_name = models.CharField(_("Заголовок новости"), max_length=128)
    date = models.DateField(_("Дата новости"), default=datetime.now)
    image = models.ImageField(_("Сменить изображение"), upload_to='news_images')
    description = models.TextField(_("Текст новости"))
    teg = models.ManyToManyField(TegiNews, verbose_name='Теги')
    tip = models.ForeignKey(to=tip_news, on_delete=models.CASCADE, verbose_name='Тип новости')
    Meta_Description = models.CharField(_("Описание (мета тег)"), max_length=156)
    news_url = models.CharField(_("URL сервиса"), max_length=256, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        # Создание уникального URL из поля name_service с транслитерацией русских символов
        if not self.news_url:
            name_translit = translit(self.articles_name, 'ru', reversed=True)
            self.news_url = slugify(name_translit)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.articles_name
    
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости' 

class articles_inner(models.Model):
    articles_name = models.CharField(_("Заголовок новости"), max_length=128)
    date = models.DateField(_("Дата статьи"), default=datetime.now)
    image = models.ImageField(_("Сменить изображение"), upload_to='articles_images')
    description = models.TextField(_("Текст статьи"))
    branch_science = models.ForeignKey(to=Otrasl, on_delete=models.CASCADE, verbose_name='Отрасль науки')
    group_specialties = models.ManyToManyField(GroupSpec, verbose_name='Группа специальностей')
    filter = models.ForeignKey(to=FilterArticle, on_delete=models.CASCADE, verbose_name='Фильтр')
    status = models.ForeignKey(to=StatusArticle, on_delete=models.CASCADE, verbose_name='Статус')
    teg = models.ManyToManyField(TegiNews, verbose_name='Теги')
    tip = models.ForeignKey(to=tip_news, on_delete=models.CASCADE, verbose_name='Тип новости')
    Meta_Description = models.CharField(_("Описание (мета тег)"), max_length=156)
    article_url = models.CharField(_("URL сервиса"), max_length=256, blank=True, null=True, unique=True)
    

    def save(self, *args, **kwargs):
        # Создание уникального URL из поля name_service с транслитерацией русских символов
        if not self.article_url:
            name_translit = translit(self.articles_name, 'ru', reversed=True)
            self.article_url = slugify(name_translit)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.articles_name
    
    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи' 

    
class Teg(models.Model):
    teg = models.TextField(_("Теги"))

    def __str__(self):
        return self.teg
    
    class Meta:
        verbose_name = 'Теги кейсов'
        verbose_name_plural = 'Теги кейсов' 

class Cases(models.Model):
    image = models.ImageField(_("Сменить изображение"), upload_to='cases_image')
    name = models.CharField(_("Имя"), max_length=128)
    description = models.TextField(_("Описание"))
    video = models.TextField(_("Ссылка на видео"))
    teg = models.ManyToManyField(Teg, verbose_name='Теги')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Кейсы'
        verbose_name_plural = 'Кейсы' 
class About(models.Model):
    name = models.CharField(_("Имя"), max_length=128)
    description = models.TextField(_("Описание"))
    image = models.ImageField(_("Сменить изображение"), upload_to='about_us_images') 

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class Activities(models.Model):
    name = models.CharField(_("Имя"), max_length=128)
    description = models.TextField(_("Описание")) 
    image = models.ImageField(_("Сменить изображение"), upload_to='educational_images')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Обучение'
        verbose_name_plural = 'Обучение'
        
class Partners(models.Model):
    image = models.ImageField(_("Сменить изображение"), upload_to='partners_image')
    name = models.TextField(_("Имя "))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Партнёры'
        verbose_name_plural = 'Партнёры'


    
class Form_Home(models.Model):
    name = models.CharField(_("Заголовок"), max_length=156)
    name_cras = models.CharField(_("Заголовок красным"), max_length=156)
    description = models.TextField(_("Текст описание"))


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Форма на главной'
        verbose_name_plural = 'Форма на главной'