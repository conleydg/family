
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from conley import views

router = DefaultRouter()
router.register(r'Movie', views.MovieViewSet)
router.register(r'Tag', views.TagViewSet)
router.register(r'People', views.PeopleViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^movie/([0-9]+)/$', views.movie_screen),
]
