from django.conf.urls import url
from .import views

urlpatterns = [
    url('^$',views.index, name= 'index'),
    url(r'^article/(?P<shortUrl>[-\w]+)/$',views.article, name= 'article'),
    url(r'^\arts/(\w+)/',views.articles, name= 'articles'),
]
