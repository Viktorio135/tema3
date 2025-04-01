from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DogViewSet, BreedViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'dogs', DogViewSet, basename='user')
router.register(r'breeds', BreedViewSet, basename='breed')


urlpatterns = [
    path('', include(router.urls)),
]
