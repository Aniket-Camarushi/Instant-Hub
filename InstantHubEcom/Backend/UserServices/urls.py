from django.contrib import admin
from django.urls import include, path
from UserServices.Controller import AuthController

urlpatterns = [
    path('login/', AuthController.LoginAPIView.as_view(), name="login"),
    path('signup/', AuthController.SignUpAPIView.as_view(), name="login"),
    path('publicAPI/', AuthController.PublicAPIView.as_view(), name="publicAPI"),
    path('protectedAPI/', AuthController.ProtectedAPIView.as_view(), name="protectedAPI"),
    path('superadminurl/',AuthController.SuperAdminCheckApi.as_view(),name='superadminurl'),
]
