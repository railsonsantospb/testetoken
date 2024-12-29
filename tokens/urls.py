from django.urls import path
from .views import TokenViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tokens', TokenViewSet)

urlpatterns = router.urls
