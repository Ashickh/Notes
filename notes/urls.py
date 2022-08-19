from django.urls import path
from notes import views
urlpatterns = [

    path("",views.index,name='emp-home'),
    path('add',views.EmployeeCreateView.as_view(),name='emp-add'),
    path('all',views.EmployeeListView.as_view(),name='emp-list'),
    path('details/<str:emp_id>',views.EmployeeDetailView.as_view(),name='emp-detail'),
    path('change/<str:emp_id>',views.EmployeeEditView.as_view(),name='emp-edit'),
    path('erase/<str:emp_id>',views.employee_remove,name='emp-del'),
    # path('accounts/signup',views.SignupView.as_view(),name='sign-up'),
    # path('accounts/signin',views.LoginView.as_view(),name='sign-in'),
    # path('accounts/signout',views.sign_out,name="sign_out")

]