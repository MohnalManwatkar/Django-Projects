from django.shortcuts import render, redirect
from .models import EmployeeTable

def homePage(request):
    emps = EmployeeTable.objects.all()
    return render(request, 'homePage.html', {'emps': emps})

def add_dataPage(request):
    if request.method == 'GET':
        return render(request,'add_dataPage.html')
    else:
        EmployeeTable(
                Emp_id = request.POST.get('emp_id'),
                Fname =request.POST.get('fname'),
                Lname = request.POST.get('lname'),
                Email_id = request.POST.get('email'),
                Contact = request.POST.get('contact'),
                Salary = request.POST.get('salary'),
                Location = request.POST.get('location')
            ).save()
        return redirect('home')
    
def update_dataPage(request, id):
    emp = EmployeeTable.objects.get(id=id)
    return render(request, 'update_data.html',{'emp':emp})

def save_updated_dataPage(request, id):
    emp = EmployeeTable.objects.get(id=id)
    emp.Emp_id = request.POST.get('emp_id')
    emp.Fname = request.POST.get('fname')
    emp.Lname = request.POST.get('lname')
    emp.Email_id = request.POST.get('email')
    emp.Contact = request.POST.get('contact')
    emp.Salary = request.POST.get('salary')
    emp.Location = request.POST.get('location')
    emp.save()
    return redirect('home')


def delete_dataPage(request, id):
    emp = EmployeeTable.objects.get(id=id)
    emp.delete()
    return redirect('home')