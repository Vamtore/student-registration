from django.db import models

class StudentRegistration(models.Model):
    """create the fields for students basic
    information, this class will create table in 
    the database according to the model fields.
    """  
    student_name = models.CharField(max_length=50)  
    student_dob = models.CharField(max_length=20)
    student_gender=models.CharField(max_length=30)
    student_address=models.CharField(max_length=155)
    student_email = models.CharField(max_length=30)  
    student_phone = models.CharField(max_length=15) 
  
    class Meta:  
        db_table = "student"
