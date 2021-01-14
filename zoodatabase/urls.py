"""zoodatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from zooapp.views import *
from zooapp import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('Index/', views.Index, name='Index'),
    path('Indexa/',views.Indexa,name='Indexa'),

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),


    path('StaffData/', StaffData ,name='StaffData'),
    path('savedata/', savedata),

    path('VisitorData/',VisitorData, name='VisitorData'),
    path('datasave/', datasave),

    path('TicketData/',TicketData, name='TicketData'),
    path('saveddata/', saveddata),

    path('SpeciesData/',SpeciesData ,name='SpeciesData'),
    path('datasaved/', datasaved),

    path('AnimalData/',AnimalData , name='AnimalData'),
    path('datasaving/', datasaving),

    path('LooksAfterData/',LooksAfterData, name='LooksAfterData'),
    path('savingdata/', savingdata),

    path('query1/',query1,name='query1'),    
    path('deletealldata/', deletealldata,name='deletealldata'),
    path('storedProcedure/',storedProcedure, name='storedProcedure'),
    path('query2/',query2,name='query2'),
    path('selectstaff/',selectstaff,name='selectstaff'),
    path('selectticket/',selectticket,name='selectticket'),
    path('selectvisitor/',selectvisitor,name='selectvisitor'),
    path('selectspecies/',selectspecies,name='selectspecies'),
    path('selectanimal/',selectanimal,name='selectanimal'),
    path('selectlooksafter/',selectlooksafter,name='selectlooksafter'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)