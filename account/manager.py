from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _ 



class CustomUserManager(BaseUserManager): 
    """Custom user model manager where email is the unique identififers
    for auth insted of username which is default for django
    """
    
    def create_user(self, email, **extra_fields): 
        """Create and save a user with given email and 
        all other fields
        
        Args: 
            email(str): email of the user
            password(str): password of the user
            
        Returns: 
            object: user object
        """
        if not email: 
            raise ValueError(_("You must enter the email of the user"))

        email = self.normalize_email(email)
        user = self.model(
            email = email, 
            **extra_fields
        )
        
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password): 
        """Create and save a super user with given information 

        Args:
            email (str): email of the super user
            password (str): password of the super user
        """
        
        user = self.create_user(email,)
        user.set_password(password)
        
        user.role = 'A'
        
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using = self._db)
        return user        
        