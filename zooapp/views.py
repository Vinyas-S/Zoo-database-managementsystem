from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from zooapp.models import *



# Create your views here.
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



@csrf_exempt
def savedata(request):
    a = int(request.POST.get("sid"))
    b = request.POST.get("sname")
    c = request.POST.get("snum")
    d = request.POST.get("sdesig")
    e = int(request.POST.get("ssalary"))
    f = request.POST.get("sdate")

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



    obje = Visitor( visitor_id=g,  name=h,  age_group=i, phone_number=j, address=k, staff_id=lk, ticket_id=tickid)
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



def deletealldata(request):
    obj=Staff.objects.all()
    obj.delete()
    msg="<h1>all the data is deleted </h1>"
    return HttpResponse(msg)
