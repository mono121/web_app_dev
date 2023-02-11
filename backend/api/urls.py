from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, UserViweSet, ManageUserView

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('users', UserViweSet)

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    path('', include(router.urls)),
]
