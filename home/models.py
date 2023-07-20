from django.db import models
from accounts.models import User
from django.utils import timezone


class Tamam_Asasy(models.Model):
    name         = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Tamam_Far3y(models.Model):
    name         = models.CharField(max_length=50, null=True, blank=True)
    tamam_asasy  = models.ForeignKey(Tamam_Asasy, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return self.name or str(self.tamam_asasy)

class Tamam(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date   = models.DateField(default=timezone.now)
    end_date     = models.DateField(default=timezone.now)
    tamam_asasy  = models.ForeignKey(Tamam_Asasy, on_delete=models.PROTECT)
    tamam_far3y  = models.ForeignKey(Tamam_Far3y, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        # print("\ntamam==>",dir(self))
        if self:
            return str(self.user) +" من " + str(self.start_date) + " إلي " + str(self.end_date)
        return str(self.user)

class Qeta3_Nadafa(models.Model):
    name        = models.CharField(max_length=30)
    weight      = models.FloatField()
    is_main     = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name
    
class Daily_Nadafa(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    qeta3_nadafa = models.ForeignKey(Qeta3_Nadafa, on_delete=models.CASCADE)
    date         = models.DateField(default=timezone.now)
    def __str__(self) -> str:
        return self.user.fullname + " حصل علي " + self.qeta3_nadafa.name + " في يوم " + str(self.date)