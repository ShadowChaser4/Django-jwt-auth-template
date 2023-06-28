from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializer import CustomTokenObtainPairSeralizer

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSeralizer
    