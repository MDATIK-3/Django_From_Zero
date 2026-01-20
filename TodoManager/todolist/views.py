from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    context = {
        'title': 'Home',
        'tasks': ['A', 'B', 'C'],
        'user': request.user
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html',{})

def tasklist(request):
    return render(request, 'tasklist.html',{})


def special_case_2003(request):
    return JsonResponse({
        'type': 'special_case_2003',
        'message': 'Hardcoded special handler for 2003'
    })

def year_archive(request, year):
    return HttpResponse(f"articles {year}")

        

def month_archive(request, year, month):
    return JsonResponse({
        'type': 'month_archive',
        'year': year,
        'month': month,
        'articles': [
            f"Article for {year}-{month:02d} - #{i}" for i in range(1, 3)
        ]
    })

def article_detail(request, year, month, slug):
    return JsonResponse({
        'type': 'article_detail',
        'year': year,
        'month': month,
        'slug': slug,
        'content': f"Detailed article {slug} for {year}-{month:02d}"
    })




def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)