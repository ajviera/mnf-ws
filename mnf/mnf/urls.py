from django.contrib.auth.models import User, Group
from django.conf.urls import url, include
from rest_framework import routers
from src import views
from src import models
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'1/users', views.UserViewSet)
router.register(r'1/groups', views.GroupViewSet)
router.register(r'1/notes', views.NoteViewSet)
router.register(r'1/tags', views.TagViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^1/admin/', admin.site.urls),
	# url(r'^1/product/(?P<pk>\d+)/mark_as_favourite/$', views.mark_as_favourite.as_view(), name='mark_as_favourite'),
	url(r'^1/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]