from django.urls import path
from .views import CustomTokenObtainPairView, RegisterView

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/", RegisterView.as_view(), name="register")
]
