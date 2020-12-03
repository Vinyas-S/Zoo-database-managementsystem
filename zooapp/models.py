from django.db import models

# Create your models here.

class Staff(models.Model):
    staff_id=models.IntegerField(primary_key=True)
    staff_name=models.CharField(max_length=30)
    contact_number=models.IntegerField()
    designation=models.CharField(max_length=30)
    salary=models.DecimalField(max_digits=10,decimal_places=3)
    joining_date=models.DateField()

    class Meta:
        db_table = "Staff"


class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    cost = models.IntegerField()
    checkin_time = models.TimeField()
    checkout_time = models.TimeField()
    payment_type = models.CharField(max_length=30)

    class Meta:
        db_table = "Ticket"



class Visitor(models.Model):
    visitor_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    age_group=models.CharField(max_length=30)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=30)
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE,related_name='%(class)s_staff_id')
    ticket_id=models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name='%(class)s_ticket_id')

    class Meta:
        db_table = "Visitor"



class Species(models.Model):
    speciesname=models.CharField(max_length=30,primary_key=True)
    population_status=models.IntegerField()

    class Meta:
        db_table = "Species"



class Animal(models.Model):
    animal_id=models.IntegerField(primary_key=True)
    animal_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=6)
    speciesname= models.ForeignKey(Species, on_delete=models.CASCADE,related_name='%(class)s_speciesname')
    birth_date=models.DateField()
    origin=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    cageno=models.IntegerField(unique=True)

    class Meta:
        db_table = "Animal"
        unique_together=(('animal_id','cageno'),)


class Looks_After(models.Model):
    animal=models.ForeignKey(Animal, on_delete=models.CASCADE,related_name='%(class)s_animal_id',primary_key=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE,related_name='%(class)s_staff_id')
    food=models.CharField(max_length=30)
    feed_time=models.TimeField()
    medicines=models.CharField(max_length=30)


    class Meta:
        db_table = "Looks_After"
        unique_together=(('animal_id','staff_id'),)
