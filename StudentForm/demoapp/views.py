from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = request.POST.get('sn')
            city = request.POST.get('sc')
            idd = request.POST.get('si')

            Student.objects.create(sname = name, scity = city, sid = idd)
        return redirect('/stu/')

    else:
        form = StudentForm()
        return render(request, 'demoapp/stu.html', {'form':form})

def update(request, id):
    data = Student.objects.get(id = id)
    initial = {'sn' : data.sname, 'sc' : data.scity, 'si' : data.sid}
    form = StudentForm(initial = initial)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            data.sname = request.POST.get('sn')
            data.scity = request.POST.get('sc')
            data.sid = request.POST.get('si')
            data.save()
        return redirect('/stu/')
    return render(request, 'demoapp.update.html', context = {'form':form, 'data':data})
