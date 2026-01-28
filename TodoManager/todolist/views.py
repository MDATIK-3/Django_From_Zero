from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import datetime

from .models import Todo, Client


def home(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if title:
            Todo.objects.create(title=title, description=description or None)

        return redirect("")
    todos = Todo.objects.all().order_by("-created_at")
    return render(request, "home.html", {"todos": todos})


def toggle_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.completed = not todo.completed
    todo.save(update_fields=["completed"])
    return redirect("home")


def Client_info(request):
    Client_info = Client.objects.all().order_by("first_name")
    return render(request, "client.html", {"data": Client_info})


def about(request):
    return render(request, "about.html", {})


def tasklist(request):
    return render(request, "tasklist.html", {})


def special_case_2003(request):
    return JsonResponse(
        {"type": "special_case_2003", "message": "Hardcoded special handler for 2003"}
    )


def year_archive(request, year):
    return HttpResponse(f"articles {year}")


def month_archive(request, year, month):
    return JsonResponse(
        {
            "type": "month_archive",
            "year": year,
            "month": month,
            "articles": [f"Article for {year}-{month:02d} - #{i}" for i in range(1, 3)],
        }
    )


def article_detail(request, year, month, slug):
    return JsonResponse(
        {
            "type": "article_detail",
            "year": year,
            "month": month,
            "slug": slug,
            "content": f"Detailed article {slug} for {year}-{month:02d}",
        }
    )


def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)
