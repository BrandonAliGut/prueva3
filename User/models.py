from django.db import models
import uuid
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

class User_Manager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Crea un usuario nuevo y lo guarda"""
        if not email:
            raise ValueError("User's mst have an Email")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, email, password):
        """ Crea un super user """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using =self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = User_Manager()
    USERNAME_FIELD = 'email'
    

class User_Perfil(models.Model):
    Genero = (
        ("F","Femenino"),
        ("M", "Masculino")
    )
    ID_DECOMPRA = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(get_user_model(), related_name="user", on_delete=models.CASCADE, unique=True)
    Nombre=models.CharField(max_length=40, blank=True, default="Indefinido")
    Apellido= models.CharField(max_length=40, blank=True, default="Indefinido")
    Sexo = models.CharField(max_length=10, choices=Genero, blank=False)
    Activo_store = models.BooleanField(default=False)
    Fecha_registro = models.DateField(auto_now_add=True)
    def __str__(self):
        return (self.Nombre)
    class Meta:
        verbose_name_plural = "Perfil Del Usuario"
        
        

def create_profile(sender, **kwargs):
    user = kwargs['instance']
    if kwargs["created"]:
        user_profile = User_Perfil(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=get_user_model())