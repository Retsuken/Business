from django.shortcuts import render, get_object_or_404
from .models import program_teacher, Reviews,service, service_faq, Person, articles_inner, Cases, About, Activities, Teg, Program, Partners, Collections_watches, Personteg, TegiNews, News, Form_Home
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def home(request):

    programs = Program.objects.all()
    services_name = service.objects.all()
    cases_all = Cases.objects.all()
    team = Person.objects.all()
    articles = News.objects.all()
    news = articles_inner.objects.all()
    filtered_products = news
    branch_science = request.GET.get('branch_science')
    group_specialties = request.GET.get('group_specialties')
    filter_value = request.GET.get('filter')
    status = request.GET.get('status')
    partner = Partners.objects.all()
    tegs = Personteg.objects.all()
    teg = request.GET.get('tegis')
    form_home = Form_Home.objects.all()
    filters = Q()

    if status:
        filters &= Q(status__Status=status)

    if branch_science:
        filters &= Q(branch_science__OtraslNauki=branch_science)

    if group_specialties:
        filters &= Q(group_specialties__GroupSpec__icontains=group_specialties)

    if filter_value:
        filters &= Q(filter__filter__icontains=filter_value)
    else:
        filtered_products = filtered_products.filter(filters)

    articles_news = News.objects.filter(tip__tip='Новости')
    articles_media = News.objects.filter(tip__tip='СМИ')
    articles_events = News.objects.filter(tip__tip='Мероприятия')
    articles_video = News.objects.filter(tip__tip='Видео')
    filtered_products = filtered_products.filter(filters)



    
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 12)
    try:
        articles = paginator.page(page_number)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)





    return render(request, 'index.html', {
        'programs': programs,
        'services_name': services_name,
        'tegs': tegs,
        'team': team,
        'cases_all': cases_all,
        'articles': articles,
        'filtered_products': filtered_products,
        'partner': partner,
        'articles_news': articles_news,
        'articles_media': articles_media,
        'articles_events': articles_events,
        'articles_video': articles_video,
        'news': news,        
        'form_home': form_home,
    })


def robots(request):
    return render(request, 'robots.html')

def sitemap(request):
    return render(request, 'sitemap.html')



def News_inner(request, news_url):
    article = get_object_or_404(News, news_url=news_url)
    articles = News.objects.all()
    current_article = News.objects.get(news_url=news_url)
    popular_articles = News.objects.exclude(news_url=news_url)
    article_tags = article.teg.all()
    tegs = TegiNews.objects.all()
    return render(request, 'article-inner-news.html', {'article': article, 'articles': articles, 'current_article': current_article, 'popular': popular_articles, 'tegs': tegs, 'article_tags': article_tags})



def all_programss(request):
    programs = Program.objects.all()
    name = request.GET.get('name') 
    filtered_products = programs



    
    if name:
        filtered_products = programs.filter(name__icontains=name)  # Фильтруем товары по названию
    return render(request, 'all-programs.html', {'programs': programs, 'filtered_products': filtered_products})

def program(request, program_url):
    programs_teacher = program_teacher.objects.all()
    reviews = Reviews.objects.all()
    program = get_object_or_404(Program, program_url__iexact=program_url)
    new_price = program.price
    if program.sale is not None:
        new_price -= (program.price * (program.sale / 100))
    return render(request, 'program.html', {'programs_teacher': programs_teacher, 'reviews': reviews, 'program': program, 'new_price': new_price})


def service_inner(request, service_url):
    services_name = service.objects.all()
    faq = service_faq.objects.all()
    team = Person.objects.all()
    services = get_object_or_404(service, service_url=service_url)

    return render(request, 'service-inner.html', {'services_name': services_name, 'team': team, 'faq': faq, 'services': services})

def person(request, person_url):
    person = get_object_or_404(Person, person_url__iexact=person_url)
    people = Person.objects.all()
    return render(request, 'person.html', {'people': people, 'person': person})

def article_inner(request, article_url):
    article = get_object_or_404(articles_inner, article_url=article_url)
    articles = articles_inner.objects.all()
    current_article = articles_inner.objects.get(article_url=article_url)
    popular_articles = articles_inner.objects.exclude(article_url=article_url)
    article_tags = article.teg.all()
    tegs = TegiNews.objects.all()
    return render(request, 'article-inner.html', {'articles': articles, 'article': article, 'current_article': current_article, 'popular': popular_articles, 'tegs': tegs, 'article_tags': article_tags})

def team_inner(request):
    teams = Person.objects.all()
    tegs = Personteg.objects.all()
    teg = request.GET.get('tegis')
    return render(request, 'team-inner.html', {'teams': teams, 'tegs': tegs})

def cases(request):
    all_cases = Cases.objects.all()
    tegs = Teg.objects.all()
    teg = request.GET.get('teg')
    filtered_products = all_cases
    if teg:
        filtered_products = filtered_products.filter(teg__teg=teg)
    return render(request, 'cases.html', {'all_cases': all_cases, 'tegs': tegs, 'filtered_products': filtered_products})

def news(request):
    articles = News.objects.all()
    articles_news = News.objects.filter(tip__tip='Новости')
    articles_media = News.objects.filter(tip__tip='СМИ')
    articles_events = News.objects.filter(tip__tip='Мероприятия')
    articles_video = News.objects.filter(tip__tip='Видео')

    page_number = request.GET.get('page')
    paginator = Paginator(articles, 12)
    try:
        articles = paginator.page(page_number)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)


    return render(request, 'all-news.html', {
        'articles': articles, 
        'article': article,
        'articles_news': articles_news,
        'articles_media': articles_media,
        'articles_events': articles_events,
        'articles_video': articles_video,
                                             })

def about(request):
    about_us = About.objects.all()
    ed_activity = Activities.objects.all()
    teams =  Person.objects.all()
    articles = articles_inner.objects.all()
    partner = Partners.objects.all()
    return render(request, 'about-us.html', {'about_us': about_us, 'ed_activity': ed_activity, 'teams': teams, 'articles': articles, 'article': article, 'partner': partner,})

def services_page(request):
    services = service.objects.all()
    services_name = service.objects.all()

    collection_id = request.GET.get('selet-category')
    if collection_id:
        services = services.filter(collections__id=collection_id)

    collections = Collections_watches.objects.all()

    return render(request, 'services-page.html', {
        'services': services,
        'services_name': services_name,
        'collections': collections
    })
def article(request):
    articles = articles_inner.objects.all()
    filtered_products = articles
    filter = request.GET.get('filter')
    last_article = articles.last()

    status = request.GET.get('status', '')
    branch_science = request.GET.get('branch_science', '')
    group_specialties = request.GET.get('group_specialties', '')
    select_category = request.GET.get('select-category', '')

    filters = Q()
    if status:
        filters &= Q(status=status)
    if branch_science:
        filters &= Q(branch_science=branch_science)
    if group_specialties:
        filters &= Q(group_specialties=group_specialties)
    if select_category:
        filters &= Q(category__name='Аналитика')

    return render(request, 'articles.html', {'articles': articles, 'filtered_products': filtered_products, 'last_article': last_article})

def mediation(request):
    programs_teacher = program_teacher.objects.all() 
    reviews = Reviews.objects.all()
    programs = Program.objects.all()
    return render(request, 'mediation.html', {'programs_teacher': programs_teacher, 'reviews': reviews, 'programs': programs})

def sign_up(request):
    programs = Program.objects.all()
    return render(request, 'sign-up.html', {'programs': programs})


def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)


    


