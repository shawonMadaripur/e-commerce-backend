from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CaroselViewSet
from django.urls import path, include
router = DefaultRouter()
router.register('product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('carosel/', CaroselViewSet.as_view()),
]
