from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Tamam_Asasy, Tamam_Far3y, Tamam, Qeta3_Nadafa
import datetime
from accounts.models import User
from django.db.models import Q

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
            if tamam_far3y[id] in "1234567890" or isinstance(tamam_far3y[id], int):
                    try:
                        tamam.tamam_far3y=Tamam_Far3y.objects.get(id=tamam_far3y[id])
                    except:
                        print("\n\n\n\nfar3y==>",tamam_far3y[id],"\n\n\n")
            tamam.save()
        return redirect("home:index")
    tamams = []
    for user in User.objects.all():

        tamam = Tamam.objects.filter(Q(start_date__lte=datetime.date.today())&
                                     Q(end_date__gte=datetime.date.today()), 
                                     user=user)        
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




def tawzee3(users, qeta3at):
    print(users, qeta3at)




def Nadafa(request):
    if request.method == "POST":
        ids = request.POST.getlist("users_ids[]")
        qeta3_ids = request.POST.getlist("qeta3_ids[]")
        users = []
        qeta3at = []
        for id in ids:
            users.append(User.objects.get(id=id))
        for qeta3_id in qeta3_ids:
            qeta3at.append(Qeta3_Nadafa.objects.get(id=qeta3_id))
        tawzee3(users, qeta3at)        
    
    
    
    # GET
    tamam = Tamam.objects.filter(
            Q(start_date__lte=datetime.date.today())&
            Q(end_date__gte=datetime.date.today()), 
        tamam_asasy=Tamam_Asasy.objects.get(name="موجود"),
                                ).exclude(tamam_far3y=Tamam_Far3y.objects.get(name="ساعي"))
    tamamOut = Tamam.objects.filter(
            Q(start_date__lte=datetime.date.today())&
            Q(end_date__gte=datetime.date.today()), 
        tamam_asasy=Tamam_Asasy.objects.get(name="موجود"),
        tamam_far3y=Tamam_Far3y.objects.get(name="ساعي"))
    return render(request, "home/nadafa.html", {"usersIn":[i.user for i in tamam], "usersOut":[i.user for i in tamamOut], "qeta3In":Qeta3_Nadafa.objects.filter(is_main=True), "qeta3Out":Qeta3_Nadafa.objects.filter(is_main=False)})