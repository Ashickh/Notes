from django.urls import path
from notes import views
urlpatterns = [

    path("",views.index,name='index'),
    path('add',views.EmployeeCreateView.as_view(),name='emp-add'),
    path('all',views.EmployeeListView.as_view(),name='emp-list'),
    path('details/<str:emp_id>',views.EmployeeDetailView.as_view(),name='emp-detail'),
    path('change/<str:emp_id>',views.EmployeeEditView.as_view(),name='emp-edit'),
    path('erase/<str:emp_id>',views.employee_remove,name='emp-del'),


]