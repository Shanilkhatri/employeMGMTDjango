from emp_app.views import *
from django.urls import path

urlpatterns = [
    path('',index_view,name='index'),
    path('view_emp',view_emp,name='view_emp'),
    path('add_emp',add_emp,name='add_emp'),
    path('remove_emp',remove_emp,name='remove_emp'),
    path('remove_emp/<int:emp_id>',remove_emp,name='remove_emp'),
    path('filter_emp',filter_emp,name='filter_emp'),
]
