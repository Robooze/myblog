from django.contrib import admin
from django.urls import re_path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import articles
from django.conf.urls.static import static
from django.conf import settings

# I am going to implement paths with REGEX (re_path)
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^articles/', include('articles.urls')),
    re_path(r'^about/$', views.about),
    re_path(r'^$', articles.views.article_list, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
