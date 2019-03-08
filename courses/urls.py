from django.conf.urls import url
from django.conf.urls import include


from rest_framework import routers

from . import views

from courses import views

from rest_framework.routers import DefaultRouter

#router = routers.SimpleRouter()
#router.register(r'courses', views.CourseViewSet)
#router.register(r'reviews', views.ReviewViewSet)

router = DefaultRouter()

router.register('course-view', views.CourseViewSet)
router.register('review-view', views.ReviewViewSet)
urlpatterns = router.urls


urlpatterns = [

    #url(r'^$', views.ListCreateCourse.as_view(), name='course_list'),
    #url(r'(?P<pk>\d+)/$', views.RetrieveUpdateDestroyCourse.as_view(), name='course_detail'),
    #url(r'(?P<course_pk>\d+)/reviews/$', views.ListCreateReview.as_view(), name='review_list'),
    #url(r'(?P<course_pk>\d+)/reviews/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyReview.as_view(), name='review_detail'),
    url(r'', include(router.urls))

    #url(r'^api/v2/', include(router.urls)),


]