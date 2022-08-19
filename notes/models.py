from django.db import models
class Employee(models.Model):
    eid=models.CharField(max_length=30,primary_key=True)
    profile_pic=models.ImageField(upload_to="profilepics",null=True)
    emp_name=models.CharField(max_length=120)

    def __str__(self):
        return self.emp_name