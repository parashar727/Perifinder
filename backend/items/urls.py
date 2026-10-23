from django.urls import path, include
from .views import ItemViewSet, KeyboardViewSet, ListingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'keyboards', KeyboardViewSet, basename='keyboard')

# Don't need listings directly accessible
# router.register(r'listings', ListingViewSet, basename='listing')

urlpatterns = [
    path('', include(router.urls))
]