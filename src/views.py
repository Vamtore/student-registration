from django.shortcuts import render
from django.shortcuts import render, redirect  
from .forms import StudentForm
from .models import StudentRegistration  

  
def addnew(request):  
    """this function is use to add new student 
    information and save it to the database.
    """
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass 
    else:  
        form = StudentForm()  
    return render(request,'index.html',{'form':form})  


def index(request):
    """this function is use to show the complete
    students information on the dashboard/home
    screen from the database.
    """  
    students = StudentRegistration.objects.all()  
    return render(request,"show.html",{'students':students})  


def edit(request, id):  
    """this function is used to edit the student 
    information and redirect student on the edit page.
    """
    student = StudentRegistration.objects.get(id=id)  
    return render(request,'edit.html', {'student':student})  


def update(request, id):
    """this function is use to save updated
    user information into the database.
    """  
    student = StudentRegistration.objects.get(id=id)  
    form = StudentForm(request.POST, instance=student)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'student': student})  


def destroy(request, id):  
    """this function is use to delete the
    spacific student object id from the
    database.
    """
    student = StudentRegistration.objects.get(id=id)  
    student.delete()  
    return redirect("/")  