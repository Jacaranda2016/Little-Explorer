from django.conf.urls import url
from .import views

urlpatterns = [
    url('volton/index',views.volton, name= 'volton'),
    url('volton/article',views.article, name= 'article'),
    url('volton/arts',views.articles, name= 'articles'),
]
