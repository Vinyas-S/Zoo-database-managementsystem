from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from zooapp.models import *
from django.shortcuts import get_object_or_404


#class MyException(Exception):
#   def showMessage(self):
#        print("this record already exists")
# Create your views here.

def Index(request):
    return render(request,'home.html')
def StaffData(request):
    return render(request,'inputdatastaff.html')
def VisitorData(request):
    return render(request,'inputdatavisitor.html')
def TicketData(request):
    return render(request,'inputdataticket.html')
def SpeciesData(request):
    return render(request, 'inputanimalspecies.html')
def AnimalData(request):
    return render(request, 'inputanimaldata.html')
def LooksAfterData(request):
    return render(request, 'inputlooksafterdata.html')



def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse("<h2>Username already taken</h2>")
                return redirect('register')
            else:
                user =User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                print("user created")
                return redirect('login')
        else:
            return HttpResponse("<h2>Password doesnt match</h2>")
            return redirect('register') 
        return redirect('/')
    
    else:    
        return render (request,'register.html')



def login(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return HttpResponse('<h2>Invalid Credentials </h2>')
            return redirect('login')    
        
    else:
        return render(request,'login.html')    



@csrf_exempt
def savedata(request):
    a = int(request.POST.get("sid"))
    b = request.POST.get("sname")
    c = request.POST.get("snum")
    d = request.POST.get("sdesig")
    e = int(request.POST.get("ssalary"))
    f = request.POST.get("sdate")
    #try:
   # ab = Staff.objects.get(staff_id=a)
        #if str(a).exists():
         #   raise MyException
        #else:
         #   pass
     #   return HttpResponse("<h1>record for this id already exists, please give a differet id</h1>")
   # except ObjectDoesNotExist:
    obj=Staff(staff_id=a,staff_name=b,contact_number=c,designation=d, salary=e,joining_date=f)
    obj.save()
    return render(request,'success.html')



@csrf_exempt
def datasave(request):
    g = int(request.POST.get("visid"))
    h = request.POST.get("visname")
    i = request.POST.get("visage")
    j = request.POST.get("visnum")
    k = request.POST.get("visaddr")
    lk = int(request.POST.get("sid"))
    try:
        staid = Staff.objects.get(staff_id=lk)
    except:
        return HttpResponse("<h1>entered staffid doesnt exist</h1>")

    kl = int(request.POST.get("ticid"))
    try:
        tickid=Ticket.objects.get(ticket_id=kl)
    except:
        return HttpResponse("<h1>entered ticketid doesnt exist</h1>")


    obje = Visitor(visitor_id=g, name=h, age_group=i, phone_number=j, address=k, staff_id=lk, ticket_id=tickid)
    obje.save()
    return render(request, 'success.html')



@csrf_exempt
def saveddata(request):
    m = int(request.POST.get("ticid"))
    n = int(request.POST.get("ticcost"))
    o = request.POST.get("ticintime")
    p = request.POST.get("ticouttime")
    q = request.POST.get("ticpay")


    objec = Ticket(ticket_id=m, cost=n, checkin_time=o, checkout_time=p, payment_type=q)
    objec.save()
    return render(request, 'success.html')



@csrf_exempt
def datasaved(request):
    r = request.POST.get("animspecies")
    s = request.POST.get("animpop")

    object = Species( speciesname=r, population_status=s)
    object.save()
    return render(request, 'success.html')



@csrf_exempt
def datasaving(request):
    t = int(request.POST.get("animid"))
    u = request.POST.get("animname")
    v = request.POST.get("animgend")
    x=request.POST.get("animspecies")
    try:
        species=Species.objects.get(speciesname=x)
    except:
       return HttpResponse ("<h1>entered species doesnt exist</h1>")

    y = request.POST.get("animbirth")
    z = request.POST.get("animorigin")
    ab = request.POST.get("animcateg")
    cd = request.POST.get("animcage")

    objects = Animal(animal_id=t, animal_name=u, gender=v, speciesname=species, birth_date=y,  origin=z, category=ab, cageno=cd)
    objects.save()
    return render(request, 'success.html')


@csrf_exempt
def savingdata(request):
    ef = int(request.POST.get("animid"))
    try:
       aniid=Animal.objects.get(animal_id=ef)
    except:
       return HttpResponse("<h1>entered animalid doesnt exist</h1>")

    gh = int(request.POST.get("sid"))
    try:
       stid = Staff.objects.get(staff_id=gh)
    except:
       return HttpResponse("<h1>entered staffid doesnt exist</h1>")

    kl = request.POST.get("animfood")
    mn = request.POST.get("animfeedtim")
    pq = request.POST.get("animmed")

    objectss = Looks_After(animal_id=ef, staff_id =gh,  food=kl,   feed_time=mn,  medicines=pq)
    objectss.save()
    return render(request, 'success.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

def deletealldata(request):
    obj=Staff.objects.all()
    obj.delete()
    msg="<h1>all the data is deleted </h1>"
    return HttpResponse(msg)


def query1(request):
    species_data = Species.objects.filter(population_status=10).values_list('speciesname')
    data = Animal.objects.filter(speciesname__in=species_data).values('animal_name','origin')
    print(data)
    return render(request, 'query1.html',{'datas':data})
    
    
    
    
    