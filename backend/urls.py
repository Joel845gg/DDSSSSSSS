from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from emotions.views import EmotionRecordViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#from emotions.views_auth import user_role


router = DefaultRouter()
router.register(r'api/emociones', EmotionRecordViewSet, basename='emociones')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('emotions.urls')),  # Esta línea ya conecta las rutas como /api/user-role/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
