from rest_framework import serializers
from rest_framework import validators

from ..models import User

class ChoiceField(serializers.ChoiceField):
    
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        
        if obj == '': 
            return None
        
        return self._choices[obj]
    
    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''
        
        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)
    

class UserSeralizer(serializers.ModelSerializer): 
    email = serializers.EmailField(
        max_length = 255, 
        validators = [validators.UniqueValidator(queryset=User.objects.all())]
    )
    role = ChoiceField(choices= User.Roles.choices)
    middle_name = serializers.CharField(max_length = 255, required = False)
    
    class Meta: 
        model = User
        fields = ("first_name", "middle_name", "last_name", "role", "id", "email")
        read_only_fields = ("id",)
    
    def create(self, validated_data): 
        user = User.objects.create(**validated_data)
        return user
        
    