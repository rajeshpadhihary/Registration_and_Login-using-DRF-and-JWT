from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_user(self,email,username,first_name,last_name,password):
        if not email:
            raise ValueError("User must have email Address !!!")
        if not username:
            raise ValueError("User must have username !!!")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,username,email,first_name,last_name,password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class customUser(AbstractBaseUser):
    email = models.EmailField(verbose_name = "email",max_length = 50,unique = True)
    username = models.CharField(max_length = 50,unique = True)
    date_joined = models.DateTimeField(verbose_name = "date_joined",auto_now_add = True)
    last_login = models.DateTimeField(verbose_name = "last_login",auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    bio = models.TextField(blank = True,null = True,max_length = 2000)
    dob = models.DateField(blank = True,null = True)
    birth_place = models.CharField(max_length = 40)
    occupation = models.CharField(max_length = 50,blank = True,null = True)
    profile_pic = models.ImageField(upload_to='image',blank=True,null=True)

    creation = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    

    def __str__(self):
        return self.username +" -- "+self.email
    
    # def has_module_perms(self,app_label):
    #     return True
    
    # def has_perm(self,perm,obj = None):
    #     return True
    
    def tokens(self):
        pass

class OneTimePassword(models.Model):
    user = models.OneToOneField(customUser,on_delete = models.CASCADE)
    code = models.CharField(max_length = 6,unique = True)

    def __str__(self):
        return f"{self.user.first_name} - passcode."
    