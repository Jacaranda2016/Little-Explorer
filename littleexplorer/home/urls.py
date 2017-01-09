from django.conf.urls import url
from .import views

urlpatterns = [
    url('volton/index',views.volton, name= 'volton'),
    url('volton/article',views.article, name= 'article'),
    url(r'^volton/arts/(\w+)/',views.articles, name= 'articles'),
]
