from django.urls import path
from .views import  Contact, SpringList, QualityExp, Ranking
from . import views

app_name = 'appname'
urlpatterns = [
    path('startspring/', views.startspring , name='spring_search'),
    path('startspring/contact.html', Contact.as_view()),
    path('startspring/springlist.html', SpringList.as_view()),
    path('startspring/qualityexp.html', QualityExp.as_view()),
    path('startspring/ranking.html', Ranking.as_view()),
    path('startspring/prefecture/', views.prefecture, name='prefecture'),
    path('startspring/prefecture/spring_each/', views.spring_each, name='springs'),
    path('startspring/search/', views.spring_search, name="search"),
]