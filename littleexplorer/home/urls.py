from django.conf.urls import url
from .import views

urlpatterns = [
    url('^$',views.index, name= 'index'),
    url(r'^article/(?P<shortUrl>[-\w]+)/$',views.article, name= 'article'),
    url(r'^category/(?P<shortUrl>[-\w]+)/$',views.category, name= 'category'),
    url(r'^articles',views.articles, name= 'articles'),
    url(r'^categories',views.categories, name= 'categories'),
]
