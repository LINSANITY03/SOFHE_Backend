from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework.urlpatterns import format_suffix_patterns
router = DefaultRouter()
router.register(r'logoutUser/', views.AuthenticationUser, basename='logout_user')

urlpatterns = router.urls
urlpatterns += [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns = format_suffix_patterns(urlpatterns)


