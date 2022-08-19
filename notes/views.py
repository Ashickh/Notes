
from django.shortcuts import render,redirect
from notes.models import Employee
from django.contrib import messages
from django.views.generic import View
from notes.forms import EmployeeCreateForm
from notes.forms import UserRegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
#
# def signin_required(fn):
#     def wrapper(request,*args,**kwargs):
#         if request.user.is_authenticated:
#             return fn(request,*args,**kwargs)
#         else:
#             messages.error(request,"User must be logged in")
#             return redirect("sign-in")
#     return wrapper

# @method_decorator(signin_required,name='dispatch')
class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeCreateForm()
        return render(request,"emp-add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=EmployeeCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()

            messages.success (request, "Note Added Successfully")
            return redirect('emp-add')
        else:
            messages.error(request,"Note Added Failed")
            return render(request,"emp-add.html",{"form":form})

# @method_decorator(signin_required,name='dispatch')
class EmployeeListView(View):
    def get(self,request,*args,**kwargs):

        ab=Employee.objects.all()
        return render(request,"emp-list.html",{'employees':ab})

# @method_decorator(signin_required,name='dispatch')
class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        ab=Employee.objects.get(eid=kwargs.get('emp_id'))
        return render(request,"emp-detail.html",{'employee':ab})

# @method_decorator(signin_required,name='dispatch')
class EmployeeEditView(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("emp_id")
        employee=Employee.objects.get(eid=eid)
        form=EmployeeCreateForm(instance=employee)
        return render(request,"emp-edit.html",{'form':form,'emp':employee})
    def post(self,request,*args,**kwargs):
        eid = kwargs.get ("emp_id")
        employee = Employee.objects.get (eid=eid)
        form=EmployeeCreateForm(request.POST,instance=employee,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Details Edited Successfully")
            return render(request,"emp-edit.html",{'form':form})
        else:
            messages.error (request, "Editing failed")
            return render (request, "emp-edit.html", {'form': form})
# @signin_required
def employee_remove(request,*args,**kwargs):
    eid=kwargs.get('emp_id')
    print(eid)
    employee=Employee.objects.get(eid=eid)
    print(employee)
    employee.delete()
    messages.success (request, "Deleted Successfully")
    return redirect("emp-list")

#
def index(request):
    return render(request,"emp-add.html")

# class SignupView(View):
#     def get(self,request,*args,**kwargs):
#         form=UserRegistrationForm
#         return render(request,"registration.html",{'form':form})
#     def post(self,request,*args,**kwargs):
#         form=UserRegistrationForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             messages.success(request,"Your registration has been successful")
#             return redirect('sign-in')
#         else:
#             print (form.cleaned_data)
#             messages.error (request, "Your registration has been failed")
#             return render(request,'registration.html',{'form':form})

# class LoginView(View):
#     def get(self,request,*args,**kwargs):
#         form=LoginForm
#         return render(request,"login.html",{'form':form})
#     def post(self,request,*args,**kwargs):
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             uname=form.cleaned_data.get("username")
#             pwd=form.cleaned_data.get("password")
#             user=authenticate(request,username=uname,password=pwd)
#             if user:
#                 login(request,user)
#                 print("success")
#
#                 return redirect("emp-list")
#             else:
#                 messages.error(request,"invalid credentials")
#                 return render (request, "login.html", {'form': form})
# # @signin_required
# def sign_out(request,*args,**kwargs):
#     logout(request)
#     return redirect("sign-in")
