from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from . import views

urlpatterns = [
    path('add-tasks/', views.TaskView.as_view(), name='add_tasks'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
