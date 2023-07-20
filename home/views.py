from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tamam_Asasy, Tamam_Far3y, Tamam
import datetime
from accounts.models import User


def index(request):
    if request.method == "POST":
        tamam_id    = request.POST.getlist("id")
        militry_id  = request.POST.getlist("militry_id")
        start_date  = request.POST.getlist("start_date")
        end_date    = request.POST.getlist("end_date")
        tamam_asasy = request.POST.getlist("tamam_asasy")
        tamam_far3y = request.POST.getlist("tamam_far3y")
        for id in range(len(tamam_id)):
            tamam = Tamam.objects.get(id=tamam_id[id])
            tamam.user = User.objects.get(militry_id=militry_id[id])
            tamam.start_date = start_date[id]
            tamam.end_date=end_date[id]
            tamam.tamam_asasy=Tamam_Asasy.objects.get(id=tamam_asasy[id])
            if isinstance(tamam_far3y[id], str) or isinstance(tamam_far3y[id], int):
                    tamam.tamam_far3y=Tamam_Far3y.objects.get(id=tamam_far3y[id])
            tamam.save()
    tamams = []
    for user in User.objects.all():
        tamam = Tamam.objects.filter(user=user, start_date__gte=datetime.date.today())
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

def get_far3y_from_asasy(request, id=None):
    return JsonResponse({
            "tamam_far3y":list(Tamam_Far3y.objects.filter(tamam_asasy=Tamam_Asasy.objects.get(id=id)).values('id', 'name'))
        })
