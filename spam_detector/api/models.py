from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, phone_number, password=None, email=None):
        if (not phone_number or not name or not password):
            raise ValueError('Users must have a phone number,name,password')

        user = self.model(
            name=name,
            phone_number=phone_number,
            email=self.normalize_email(email) if email else None

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, phone_number, password, email=None):
        user = self.create_user(name, phone_number, password, email)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    # password = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15, unique=True)
    userid = models.AutoField(primary_key=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name','phone_number',]

    objects = UserManager()

    def __str__(self):
        return self.phone_number


# class Spam(models.Model):
#     number = models.CharField(max_length=10)
#     count = models.IntegerField()
#     reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spam')
#     timestamp = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.number


# class Contacts(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     number = models.CharField(max_length=15)

#     def __str__(self):
#         return f'{self.name} - {self.number}'
