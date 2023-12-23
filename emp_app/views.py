from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import *
from django.db.models import Q
# Create your views here.
def index_view(request):
    return render(request,'index.html')

def view_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request,'view_emp.html', context)

def add_emp(request):
    if request.method == "POST":
        print(request.POST.dict())
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        dept = int(request.POST["dept"])
        salary = int(request.POST["salary"])
        phone = int(request.POST["phone"])
        bonus = int(request.POST["bonus"])
        role_id = int(request.POST["role"])
        department = get_object_or_404(Department, pk=dept)
        role = get_object_or_404(Role, pk=role_id)
        new_emp = Employee(first_name=first_name,last_name=last_name,dept=department,salary=salary,phone=phone,bonus=bonus,role=role)
        new_emp.save()
        
        # get all emps
        emps = Employee.objects.all()
        context = {
            'emps': emps
        }
        return render(request,'view_emp.html', context)
    else:
        return render(request,'add_emp.html')

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            emps = Employee.objects.all()
            context = {
            'emps': emps
            }
            return render(request,'view_emp.html',context)
        except:
            return HttpResponse("enter a valid user Id")
    emps = Employee.objects.all()
    context = {
    'emps': emps
    }    
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == "POST":
        name = request.POST["name"]
        dept = request.POST["dept"]
        role = request.POST["role"]
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__role__icontains=role)
        
        context = {
            "emps": emps
        }
        return render(request,'view_emp.html', context)
    return render(request,'filter_emp.html')
