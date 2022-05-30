
from django.urls import re_path as url
from . import views

urlpatterns=[
    url(r'^$',views.news_today,name='newsToday'),
    
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^article/(\d+)',views.article,name ='article')
    
]
