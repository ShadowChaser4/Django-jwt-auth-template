from rest_framework.views import APIView
from rest_framework import permissions, status, response
from django.db.models import Q
from drf_yasg import openapi 
from drf_yasg.utils import swagger_auto_schema


from ..serializer import UserSerializer
from ..models import User

class UserView(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    query_set = User.objects.all()
    
    @swagger_auto_schema(
        operation_description="POST /users/",
        request_body= openapi.Schema(
            type= openapi.TYPE_OBJECT, 
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                'middle_name': openapi.Schema(type=openapi.TYPE_STRING),         
            }, 
            required= ['email', 'password','first_name','last_name']
        ), 
        responses= {200: UserSerializer()}
        )
    def post(self, request): 
        data = request.data
                
        seralizer = self.serializer_class(data = data)
        seralizer.is_valid(raise_exception= True)
        user = seralizer.save()
        
        seralized_data = self.serializer_class(instance= user).data
        
        return response.Response(data = seralized_data, status= status.HTTP_201_CREATED)
    
    @swagger_auto_schema(responses={200: UserSerializer(many = True)})
    def get(self, reqeust):
        query = reqeust.GET.get("query",'')
                
        seralizer = self.serializer_class
        
        hits = self.query_set.filter(
            Q(first_name__icontains = query),
            Q(email__icontains = query)
        ).order_by('first_name', 'email')
        
        
        data = seralizer(hits, many= True).data
        return response.Response(
            data= data
        )
        
        
        
    
    