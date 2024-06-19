from django.db import models

# # Create your models here.  
# class member(models.Model):  
#     mid      = models.CharField(max_length=20)  
#     mname    = models.CharField(max_length=100)  
#     mcontact = models.CharField(max_length=15)  
#     class Meta:  
#         db_table = "member"  


class student(models.Model):
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)  
    contact    = models.IntegerField()  
    email      = models.EmailField(max_length=50)  
    age        = models.IntegerField()  

    class Meta:
        db_table = "studentapp"