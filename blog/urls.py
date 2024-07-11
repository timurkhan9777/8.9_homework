from django.urls import path,include
from .views import CategoryAPIView,PostAPIView,CommentAPIView,LikeAPIView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers
router = routers.DefaultRouter()
router.register("category",CategoryAPIView)
router.register("post",PostAPIView)
router.register("comment",CommentAPIView)
router.register("like",LikeAPIView)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('auth/',include('djoser.urls')),
    path('auth/token/',include('djoser.urls.authtoken')),
]