from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'train', views.test)
router.register(r'predict', views.GroupViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
