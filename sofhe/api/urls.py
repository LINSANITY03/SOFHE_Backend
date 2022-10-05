from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from . import views

urlpatterns = [
    path('add-tasks/<int:pk>', views.addUserTask, name='add_tasks'),
    path('all-tasks/<int:pk>', views.userTask, name='all_tasks'),
    path('edit-tasks/<int:taskId>/<int:pk>',
         views.editUserTask, name='edit_tasks'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
