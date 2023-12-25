from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import response
from .models import Signin

#//////////////////////////////////////////////////////|
# Create your views here.                            
def first_of_all(request):                           
    return render(request, 'pages/First_Of_All.html')

def home_page(request):
    return render(request, 'pages/Home_Page.html')
#//////////////////////////////////////////////////////
def sign_in(request):
    id = request.POST.get("id")
    Fname = request.POST.get("Fname")
    Lname = request.POST.get("Lname")
    date = request.POST.get("date")
    gpa = request.POST.get("gpa")
    gender = request.POST.get("gender")
    level = request.POST.get("level")
    status = request.POST.get("status")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    dep = request.POST.get("dep")
    if(dep == None):
        dep = 'General'
    if any(field is None or field == '' for field in [id, Fname, Lname, date, gpa, gender, level, status, email, phone]):
        return render(request, 'pages/Sign_In.html')
    users = Signin.objects.filter(id=id)
    emails = Signin.objects.filter(email=email)
    if len(users) == 0 and len(emails) == 0:
        data = Signin(id=id, Fname=Fname, Lname=Lname, date=date, gpa=gpa, gender=gender, level=level, status=status, email=email, phone=phone, dep=dep)
        data.save()
        alert_script = """
            <script>
                alert("Student has been saved successfully!");
                window.location.href = "/signin";
            </script>
            """
        return HttpResponse(alert_script.format(id=id, email=email))
    else:
        alert_script = """
            <script>
                alert("Student Found before, plz check the id or email!");
                window.location.href = "/signin";
            </script>
            """
        return HttpResponse(alert_script.format())

#//////////////////////////////////////////////////////////////////////////////////////////

def sign_in_for_update(request):
    id = request.GET.get("id")
    email = request.GET.get("email")
    if any(field is None or field.strip() == '' for field in [id, email]):
        return render(request, 'pages/Sign_In_For_Update.html')
    
    users = Signin.objects.filter(id=id)    
    if len(users) != 0:
        registered = users[0]
        
        if email == registered.email:
            return redirect('update_info', id=registered.id, email=registered.email)
        else:
            alert_script = """
            <script>
                alert("Email doesn't match , try again!");
                window.location.href = "/signinforupdate";
            </script>
            """
            return HttpResponse(alert_script.format(id=id, email=email))
    else:
        alert_script = """
        <script>
            alert("ID Not Found!");
            window.location.href = "/signinforupdate";
        </script>
        """
        return HttpResponse(alert_script.format(id=id, email=email))

#//////////////////////////////////////////////////////////////////////////////////////////
def search_activity(request):
    return render(request, 'pages/Search_Activity.html')

def search(request):
    if request.method == 'GET':
        result = Signin.objects.all().values()
        return JsonResponse(list(result), safe=False)
#//////////////////////////////////////////////////////////////////////////////////////////
def all_status(request):
    return render(request, 'pages/All_Status.html')
#//////////////////////////////////////////////////////////////////////////////////////////

def update_status(request):
    if request.method == 'POST':
        student_id = request.POST.get('id')
        new_status = request.POST.get('status')

        try:
            student = Signin.objects.get(id=student_id)
            student.status = new_status
            print(new_status)
            student.save()
            return JsonResponse({'message': 'Status updated successfully'})
        
        except Signin.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

#//////////////////////////////////////////////////////////////////////////////////////////
def remove_student(request, student_id):
    try:
        student = Signin.objects.get(id=student_id)
        student.delete()
        return redirect('home_page')
    except Signin.DoesNotExist:
        return redirect('home_page')
#//////////////////////////////////////////////////////////////////////////////////////////
def update_info(request, id, email):
    users = Signin.objects.filter(id=id)
    if len(users) == 0 or users[0].email != email:
        return redirect('sign_in_for_update')
    registered = users[0]
    context = {
        'id': id,
        'email': email,
        'registered': registered,
    }
    if request.method == 'POST':
        if 'remove_student' in request.POST:
            remove_student(request,id)
            alert_script = """
            <script>
                alert("Student has been deleted successfully.");
                window.location.href = "/signinforupdate/";
            </script>
            """
            return HttpResponse(alert_script.format())
        else:
            try:
                update = Signin.objects.get(id=id)
            except Signin.DoesNotExist:
                return redirect('sign_in_for_update')

            update.gpa = request.POST.get('gpa')
            update.level = request.POST.get('level')
            update.status = request.POST.get('status')
            update.email = request.POST.get('email')
            update.phone = request.POST.get('phone')
            update.dep = request.POST.get('dep')
            if(update.dep == None):
                update.dep = 'General'
            update.save()

            alert_script = """
            <script>
                alert("Student information has been updated successfully.");
                window.location.href = "/update_info/{id}/{email}";
            </script>
            """
            return HttpResponse(alert_script.format(id=id, email=email))
    return render(request, 'pages/Update_Info.html', context)
#//////////////////////////////////////////////////////////////////////////////////////////