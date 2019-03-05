from django.conf.urls import url
from django.conf.urls import include


from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [

    url(r'^$', views.ListCourse.as_view(), name='course_list')

]