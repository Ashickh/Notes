from django import forms
from notes.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=[

            "profile_pic",
            "emp_name"
        ]

        widgets={

            "emp_name": forms.Textarea (attrs={'class': "form-control"}),
            "profile_pic": forms.FileInput (attrs={'class': "form-control rounded-pill"}),


        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            "first_name",
                "last_name",
                "email",
                "username",
                "password1",
                "password2",
        ]

        widgets = {
            "first_name": forms.TextInput (attrs={'class': "form-control rounded-pill"}),
            "last_name": forms.TextInput (attrs={'class': "form-control rounded-pill"}),
            "email": forms.EmailInput (attrs={'class': "form-control rounded-pill"}),
            "username": forms.TextInput (attrs={'class': "form-control rounded-pill"}),
            "password1": forms.PasswordInput (attrs={'class': "form-control rounded-pill"}),
            "password2": forms.PasswordInput (attrs={'class': "form-control rounded-pill"})

        }






class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
#
# class RegForm(forms.Form):
#     f_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter First Name"}))
#     l_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Last Name"}))
#     e_mail=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Email"}))
#     u_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Username"}))
#     pwd=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter password"}))

# class EmployeeCreateForm(forms.Form):
#     eid=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Emp ID"}))
#     emp_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-pill", "placeholder":"Enter Name"}))
#     desig=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Designation"}))
#     salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Salary"}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Email"}))
#     experience=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Experience"}))

    # def clean(self):
    #     cleaned_data=super().clean()
    #     exp=cleaned_data.get("experience")
    #     if exp<0:
    #         msg="Invalid Exp"
    #         self.add_error("experience",msg)

