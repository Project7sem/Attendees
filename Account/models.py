from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

#manager for our custom model 
class MyAccountManager(BaseUserManager):
    """
        This is a manager for Account class 
    """
    # Method for  creating new user
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an Emaill address")
        if not username :
            raise ValueError("Users must have an Username")
        user  = self.model(
                email=self.normalize_email(email),
                username=username,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user
    # Method for creating super user.
    def create_superuser(self, email, username, password):
        user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,
            )
        user.is_admin = True
        user.is_staff=True
        user.is_superuser=True
        user.is_university = True 
        user.is_colleges = True 
        user.is_student = True
        user.save(using=self._db)
        return user


#Custom base class for email authentication
class CustomUser(AbstractUser):   
    """
      Custom user class inheriting AbstractBaseUser class 
    """
    
    email                = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username             = models.CharField(max_length=30,unique=True)
    date_joined          = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login           = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin             = models.BooleanField(default=False)
    is_active            = models.BooleanField(default=True)
    is_staff             = models.BooleanField(default=False)
    is_superuser         = models.BooleanField(default=False)
    is_university        = models.BooleanField(default=False)
    is_colleges          = models.BooleanField(default=False)
    is_student           = models.BooleanField(default=False)

    #Defines email is in username field.
    USERNAME_FIELD = ('email')

    #Username is required
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label ):
        return True


