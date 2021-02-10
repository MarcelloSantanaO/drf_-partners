from django.urls import include, path
from rest_framework import routers
from .views import PartnerViewSet
from .views import PartnerApi

router = routers.DefaultRouter()
router.register(r'partners', PartnerViewSet, basename='partners')

urlpatterns = [
    path('', include(router.urls)),
    path('partners/api', PartnerApi.as_view()),
    path('api-auth', include('rest_framework.urls', namespace='drf_partners'))
]