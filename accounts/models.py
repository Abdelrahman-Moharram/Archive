from django.db import models
from django.contrib.auth.models import User,BaseUserManager,AbstractBaseUser, AbstractUser




class Moahl_Type(models.Model):
    name        = models.CharField(max_length=20)
    duration    = models.FloatField()
    def __str__(self):
        return self.name


class Rank (models.Model):
    name    = models.CharField(max_length=20)
    rank    = models.IntegerField()
    def __str__(self):
        return self.name

class Work_Category (models.Model):
    name    = models.CharField(max_length=20)
    def __str__(self):
        return self.name



### ----- ####
class accountManager(BaseUserManager):
    def create_user(self,militry_id,fullname,password = None):
        if not militry_id:
            raise ValueError('user must have an militry_id')

        if not fullname:
            raise ValueError('Unvalid Null Value for fullname')
        
        user = self.model(
            militry_id = militry_id,
            fullname = fullname,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    

    def create_superuser(self,militry_id,fullname,password):
        user = self.create_user(
            militry_id = militry_id,
            fullname = fullname,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 







class User(AbstractBaseUser):
    fullname        = models.CharField(max_length=50,verbose_name="Full Name",unique=False)
    militry_id      = models.CharField(unique = True, max_length=30)
    password        = models.CharField(max_length=150)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    moahl           = models.CharField(max_length=150, null=True)
    moahl_type      = models.ForeignKey(Moahl_Type, null=True, on_delete=models.PROTECT)
    rank            = models.ForeignKey(Rank, null=True, on_delete=models.PROTECT)
    work_category   = models.ForeignKey(Work_Category, null=True, on_delete=models.PROTECT)
    tagned_date     = models.DateField(null=True, blank=True)
    end_date        = models.DateField(null=True, blank=True)

    def phones(self):
        return Users_Phone.objects.filter(user=self)

    USERNAME_FIELD  = 'militry_id'
    REQUIRED_FIELDS = ['fullname']

    objects = accountManager()
    def save(self, *args, **kwargs):
        # Save the provided password in hashed format
        user = super(User, self)
        user.set_password(self.password)
        super().save(*args, **kwargs)
        return user

    def __str__(self):
        return self.fullname

    def has_perm(self , perm , obj = None):
        return self.is_superuser
    
    def has_module_perms(self,app_label):
        return self.is_staff





class Users_Phone(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    phone       = models.CharField(max_length=12)

    def __str__(self):
        return str(self.user) + ' ' + str(self.phone)