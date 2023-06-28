from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSeralizer(TokenObtainPairSerializer): 
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        
        del data['refresh']
        data['success'] = True
        
        return data
        
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['name'] = user.get_full_name()
        token['role'] = user.get_role_display()
        
        return token