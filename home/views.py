from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tamam_Asasy, Tamam_Far3y, Tamam
import datetime
from accounts.models import User


def index(request):
    tamams = []
    for user in User.objects.all():
        tamam = Tamam.objects.filter(user=user, start_date__gte=datetime.date.today())
        print("==>",tamam)
        if not tamam:
            tamam = Tamam.objects.create(user=user)
            tamams.append(tamam)
        else:
           tamams.append(tamam[0])
    return render(request, "home/index.html", {
        "tamams":tamams,
        "tamam_asasy":Tamam_Asasy.objects.all(),
        "tamam_far3y":Tamam_Far3y.objects.all()
        })

def get_far3y_from_asasy(request, tamam_asasy=None):
    print("==>tamam", tamam_asasy)
    return JsonResponse({
            "tamam_far3y":list(Tamam_Far3y.objects.filter(tamam_asasy=Tamam_Asasy.objects.get(id=1)).values('id', 'name'))
        })
    # return HttpResponse('Bad Request')