from django.contrib.auth.models import AbstractUser
from django.db import models 
from django.utils.translation import gettext_lazy as _

from ..manager import CustomUserManager

class User(AbstractUser):
    """Custom user model where email is the unique identifier and 
    user have middle name that is optional
    """
    
    class Roles(models.TextChoices):
        ADMIN = 'A',_("Admin")
        USER = 'U', _("User")
    
    username = None
    email = models.EmailField(unique= True)
    middle_name = models.CharField(max_length=255, null= True, blank= True)
    is_superuser = models.BooleanField(default= False)
    role = models.CharField(max_length=1, choices= Roles.choices)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    
    class Meta: 
        app_label = 'account'
        
    def __str__(self) -> str:
        return self.email
    
    def get_full_name(self) -> str:
        middle_name = f'{self.middle_name} ' if self.middle_name is not None else ''
        return f'{self.first_name} {middle_name}{self.last_name}'
    
    
