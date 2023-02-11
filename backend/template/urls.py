from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from api.views import TaskViewSet, UserViweSet, ManageUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/', include('djoser.urls.jwt'))
]

