from django.urls import path, include
from . import views
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404



handler404 = 'mainapp.views.custom_page_not_found'


urlpatterns = [
    re_path(r'^@(?P<news_url>[\w-]+)(?:/)?$', views.News_inner, name='news'),
    path('summernote/', include('django_summernote.urls')),
    re_path(r'^(?!%s)(?P<program_url>\w+)/$' % settings.STATIC_URL.lstrip('/'), views.program, name='program'),
    path('<path:service_url>/', views.service_inner, name='service_inner'),
    re_path(r'^~(?P<article_url>[\w-]+)(?:/)?$', views.article_inner, name='article_inner'),
    re_path(r'^(?P<person_url>[\w-]+)(?:/)?$', views.person, name='person'),
    path('', views.home, name='home'),
    path('all-programs.html', views.all_programss, name='all_programs'),
    path('team-inner.html', views.team_inner, name='team_inner'),
    path('cases.html', views.cases, name='cases'),
    path('all-news.html', views.news, name='all_news'),
    path('about-us.html', views.about, name='about_us'),
    path('services-page.html', views.services_page, name='service_page'),
    path('articles.html', views.article, name='all_articles'),
    path('mediation.html', views.mediation, name='mediation'),
    path('sign-up.html', views.sign_up, name='sign_up'),
    path('robots.txt', views.robots, name='robots'),
    path('sitemap.xml', views.sitemap, name='sitemap')
]
