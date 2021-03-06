from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^search/', views.search, name='search'),
    url(r'^myprofile/', views.myprofile, name='myprofile'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^comment/(\d+)',views.comment,name='comment'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)