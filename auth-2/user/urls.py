from django.urls import path
from .views import CustomObtainPairView

urlpatterns = [
    path('login/', CustomObtainPairView.as_view(), name='token_obtain_pair'),
]
