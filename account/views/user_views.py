from rest_framework.views import APIView
from rest_framework import permissions, status, response
from django.db.models import Q

from ..serializer import UserSeralizer
from ..models import User

class UserView(APIView):
    seralizer_class = UserSeralizer
    permission_classes = [permissions.IsAuthenticated]
    query_set = User.objects.all()
    
    def post(self, request): 
        data = request.data
                
        seralizer = self.seralizer_class(data = data)
        seralizer.is_valid(raise_exception= True)
        user = seralizer.save()
        
        seralized_data = self.seralizer_class(instance= user).data
        
        return response.Response(data = seralized_data, status= status.HTTP_201_CREATED)
    
    def get(self, reqeust):
        query = reqeust.GET.get("query",'')
                
        seralizer = self.seralizer_class
        
        hits = self.query_set.filter(
            Q(first_name__icontains = query),
            Q(email__icontains = query)
        ).order_by('first_name', 'email')
        
        
        data = seralizer(hits, many= True).data
        return response.Response(
            data= data
        )
        
        
        
    
    