from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name= 'about'),
    path("tasklist/", views.tasklist, name='tasklist'),
    path("client/", views.Client_info, name='client_info'),
    path("toggle/<int:id>/", views.toggle_todo, name="toggle_todo"),



    
    path("articles/2003/", views.special_case_2003),
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
    path("current_datetime/", views.current_datetime)
]