from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import response
from student.models import Student

# Create your views here.
# def add_student(request):
#     if request.method == 'POST':
#         # Retrieve the data sent via AJAX
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         ID = request.POST.get('ID')
#         mail = request.POST.get('mail')
#         phone = request.POST.get('phone')
#         gender = request.POST.get('gender')
#         level = request.POST.get('level')
#         department = request.POST.get('department')
#         status = request.POST.get('status')
#         gpa = request.POST.get('gpa')
#         birth_date = request.POST.get('birth_date')

#         if Student.objects.filter(id=ID).exists() or Student.objects.filter( email = mail):
#             return HttpResponse("Error: Student already exists")
#         else:
#             new_student = Student(firstname=first_name, lastname=last_name, id=ID, email=mail, phone=phone,
#                                 gender=gender, level=level, department=department, status=status, GPA=gpa,
#                                 birthdate=birth_date)
#             new_student.save()
#             return HttpResponse("Student added successfully")
# def get_data(request):
#     data = Student.objects.all().values()
#     return JsonResponse(list(data), safe=False)


# def add_student(request):
#     if request.method == 'POST':
#         student = Student()
#         student.id = request.POST.get('id')
#         student.first_name = request.POST.get('Fname')
#         student.last_name = request.POST.get('Lname')
#         student.birthdate = request.POST.get('date')
#         student.gpa = request.POST.get('gpa')
#         student.gender = request.POST.get('gender')
#         student.level = request.POST.get('level')
#         student.status = request.POST.get('status')
#         student.email = request.POST.get('email')
#         student.phone = request.POST.get('phone')
#         student.department = request.POST.get('dep')
#         student.save()
#         return redirect('success')  # Redirect to a success page
#     return render(request, 'add_form.html')


def add_student(request):
    id = request.POST.get('id')
    first_name = request.POST.get('Fname')
    last_name = request.POST.get('Lname')
    date_of_birth = request.POST.get('date')
    gpa = request.POST.get('gpa')
    gender = request.POST.get('gender')
    level = request.POST.get('level')
    status = request.POST.get('status')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    department = request.POST.get('dep')

    student = Student(
        id=id,
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        gpa=gpa,
        gender=gender,
        level=level,
        status=status,
        email=email,
        phone=phone,
        department=department
    )
    print(first_name)
    student.save()
    return redirect('home_page')  # Redirect to the desired page after saving