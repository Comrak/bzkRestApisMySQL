
from mangas import views 
from django.urls import include, re_path
urlpatterns = [ 
    re_path(r'^api/mangas$', views.manga_list),
    re_path(r'^api/mangas/(?P<pk>[0-9]+)$', views.manga_detail),
    re_path(r'^api/mangas/published$', views.manga_list_published)
]
