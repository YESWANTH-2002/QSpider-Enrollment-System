# enrollment/views.py
from django.shortcuts import render, redirect
from .forms import EnrollmentForm
from .models import Student

def enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollment/enrollment.html', {'form': form})

def edit_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EnrollmentForm(instance=student)
    return render(request, 'enrollment/edit_student.html', {'form': form, 'student': student})

def success(request):
    students = Student.objects.all()
    return render(request, 'enrollment/success.html', {'students': students})
