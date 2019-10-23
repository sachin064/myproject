from django.conf.urls import  url, include
from django.urls import path
from rest_framework import routers
from .views import CarSearchView,signup
# router = routers.DefaultRouter()
# router.register('car/search', CarSearchView,basename='car')
# urlpatterns = router.urls

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
]