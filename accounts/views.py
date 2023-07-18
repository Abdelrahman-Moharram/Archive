from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User, Work_Category, Moahl_Type, Rank
from .forms import add_user_form
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, "accounts/index.html", {"users":User.objects.all()})

@login_required
def addUser(request):
    form   = add_user_form()
    if request.method == "POST":
        form = add_user_form(request.POST)

        if form.is_valid():
            form = form.save()
            messages.info(request,form.fullname+" added succesfully")
            if "_submit" in  request.POST:
                return redirect("accounts:add")
            return redirect("accounts:index") # جدول فيه كل اليوزرز
    return render(request,"accounts/addUser.html",{"form":form,
                                                   "workCategories":Work_Category.objects.all(),
                                                    "moahltypes":Moahl_Type.objects.all(),
                                                    "ranks":Rank.objects.all()
                                                })



def register(request):
    if request.user.is_authenticated:
        return redirect("home:index")
    form   = add_user_form()
    if request.method == "POST":
        form = add_user_form(request.POST)
        if form.is_valid():
            form = form.save()

            # after saving form we should signin to account
            user = authenticate(request, username=request.POST['militry_id'], password=request.POST['password'])
            if user is not None:
                print("\n\n\nuser==>", user)
                login(request, user)
                ## save date in session should be string not date -> we made [tagned_date, end_date] in str form
                user._mutable = True
                user.tagned_date = str(user.tagned_date)
                user.end_date = str(user.end_date)

                # save user in sessions
                request.session.user = user
            
                # logged in successfully after regestration
                messages.info(request,form.fullname+" added succesfully")
                return redirect("accounts:profile", militry_id=form.militry_id) # تمام القوة انهارده
            
            # logged in Failed after regestration
            messages.error(request,"Login Failed after registeration contact admin")
            return redirect("accounts:register")
        # Registration failed
        messages.error(request,"Registration failed")
        return redirect("accounts:register")
    
    # GET request should pass here
    return render(request,"accounts/register.html",{"form":form, 
                                                    "workCategories":Work_Category.objects.all(),
                                                    "moahltypes":Moahl_Type.objects.all(),
                                                    "ranks":Rank.objects.all()
                                                })




def user_login(request):
    if request.user.username:
        return redirect("home:index")
    if request.method == "POST":
        user = authenticate(request, username=request.POST['militry_id'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            ## save date in session should be string not date -> we made [tagned_date, end_date] in str form
            user._mutable = True
            user.tagned_date = str(user.tagned_date)
            user.end_date = str(user.end_date)

            # save user in sessions
            request.session.user = user

            # logged in successfully
            messages.info(request," أهلا "+request.user.fullname+" مرحبا بعودتك")
            return redirect("accounts:profile", militry_id=request.user.militry_id) # تمام القوة انهارده
        
        # no user 
        messages.error(request,"فشل تسجيل الدخول تأكد من الرقم العسكري وكلمة المرور")
        return redirect("accounts:login")
    # get request - NOT POST
    return render(request,"accounts/login.html",{})



@login_required
def profile(request,militry_id):
    return render(request,"accounts/profile.html",{"user":User.objects.get(militry_id=militry_id)})


@login_required
def logout_user(request):
        logout(request)
        return redirect("home:index")

@login_required
def edit(request, militry_id):
    user = User.objects.get(militry_id=militry_id)
    if  request.method == "POST":
        user.fullname = request.POST['fullname']
        user.militry_id = request.POST['militry_id']
        user.moahl = request.POST['moahl']
        user.work_category = Work_Category.objects.get(id=request.POST['work_category'])
        user.moahl_type = Moahl_Type.objects.get(id=request.POST['moahl_type'])
        user.rank = Rank.objects.get(id=request.POST['rank'])
        user.tagned_date = request.POST['tagned_date']
        user.end_date = request.POST['end_date']
        user.password = request.POST['password']
        user.retypepassword = request.POST['retypepassword']
        user.save()
        messages.info(request,"تم تعديل بيانات "+user.fullname+ " بنجاح")
        return redirect("accounts:index")
    return render(request,"accounts/addUser.html",{"user":user,
                                                   "workCategories":Work_Category.objects.all(),
                                                    "moahltypes":Moahl_Type.objects.all(),
                                                    "ranks":Rank.objects.all()
                                                })
@login_required
def delete(request, militry_id):
    user = User.objects.get(militry_id=militry_id)
    user.delete()
    return redirect("accounts:index")