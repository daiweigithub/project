from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from asm import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'records', views.RecordViewSet)
router.register(r'userrecords', views.UserRecordViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += router.urls
