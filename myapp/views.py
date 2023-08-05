from django.http import HttpResponse
from django.shortcuts import redirect, render

from myapp.forms import programForm
from . models import projectdetail

# Create your views here.
def index(request):
    return HttpResponse('senif parasara')  #use of app

def view_data(request):
    return render(request,'forms.html')   #view form

# def stor_data(request):
#     return render(request,'forms.py')

def stor_data(request):
    if request.method=="POST":
        form = programForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myapp/showdata')
                
    
    return render(request,'forms.html',{'form':form})


def showdata(request):
    student = projectdetail.objects.all()
    return render(request,"show.html",{'student':student})

def updaterecord(request,rollno):
    data = projectdetail.objects.get(roll_no=rollno)
    data.g_no = request.POST['g_no']
    data.roll_no = request.POST['roll_no']
    data.enr_no = request.POST['enr_no']
    data.name = request.POST['name']
    data.div = request.POST['div']
    data.pro_det = request.POST['pro_det']
    data.save()
    return redirect('/myapp/showdata')

# def updaterecord(request,rollno):
#     students = projectdetail.objects.get(roll_no=rollno)
#     form = programForm(request.POST, instance = students)
#     if form.is_valid():
#         form.save()
#         return redirect("/myapp")
#     return render(request,'updatedata.html', {'students':student})

def delete_data(request,rollno):
    data = projectdetail.objects.get(roll_no=rollno)
    data.delete()
    return redirect('/myapp/showdata')

def editdata(request,rollno):
    students = projectdetail.objects.get(roll_no=rollno)
    return render(request,'updatedata.html', {'students':student})
