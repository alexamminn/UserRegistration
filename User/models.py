from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.
class manage_user(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
        if not username or username==' ':
            raise ValueError('Invalid Username!')
        if not email:
            raise ValueError('Invalid Email!')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, first_name, last_name, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_staff=True
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class models_user_registration(AbstractBaseUser):
    username            = models.CharField(unique=True, max_length=50, verbose_name='Username')
    email               = models.EmailField(unique=True, max_length=50, verbose_name='Email')
    first_name          = models.CharField(verbose_name='First Name', max_length=20)
    last_name           = models.CharField(verbose_name='Last Name', max_length=20)
    last_login          = models.DateField(verbose_name='Last Login', auto_now=True)
    join_date           = models.DateField(verbose_name='Date Joined', auto_now_add=True)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_admin            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

    objects = manage_user()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_Label):
        return True
    
    class Meta:
        verbose_name = 'User List'
        verbose_name_plural = 'Registered User'
