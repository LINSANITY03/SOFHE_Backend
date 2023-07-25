from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.EventTask, basename='event')
urlpatterns = router.urls
