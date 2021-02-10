from django.urls import include, path
from rest_framework import routers
from .views import PartnerViewSet


router = routers.DefaultRouter()
router.register(r'partners', PartnerViewSet, basename='partners')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='drf_partners'))
]