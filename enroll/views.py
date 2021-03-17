from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from .forms import Student
from .models import User
# Create your views here.
# This function adds a new item and show all the items
def add_show(request):
    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pwd)
            reg.save()
            fm = Student()
#            fm.save()
    else:
        fm = Student()
    vision = User.objects.all()
    return render(request,'enroll/show.html', {'form':fm,'st':vision})

# This will edit or update the selected item
def update_data(request,id):
    if request.method == 'POST':
        obj = User.objects.get(pk=id)
        fm = Student(request.POST, instance=obj)
        if fm.is_valid():
            fm.save()
    else:
        obj = User.objects.get(pk=id)
        fm = Student(instance=obj)
    return render(request, 'enroll/update.html',{'form':fm})


# This function will delete the item
def delete_data(request, id):
    if request.method == 'POST':
        obj = User.objects.get(pk=id)
        obj.delete()
        return HttpResponseRedirect('/')