from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmotionRecordViewSet
from .views_auth import RegisterView, user_role  # ✅ Solo importa lo necesario

router = DefaultRouter()
router.register(r'emotions', EmotionRecordViewSet, basename="emotions")

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user-role/', user_role, name='user-role'),  # ✅ Esto sí se usa
    path('', include(router.urls)),
]
