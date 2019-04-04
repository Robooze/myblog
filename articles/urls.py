from django.urls import re_path
from . import views

app_name = 'articles'  # Namespacing this urls file

urlpatterns = [
    re_path(r'^$', views.article_list, name='list'),  # giving a url name which we can link to later on
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
]
