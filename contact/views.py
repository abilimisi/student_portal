

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages

from .models import BSc_Admission_Form,UG_Study,Notification,Gallery
from django.template.loader import get_template


from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import StudentSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Result,UG_Course
from django.contrib.auth.models import User
from django.http import HttpResponse



# Create your views here.
def index(request):
    student = None
    if request.user.is_authenticated:
        try:
            student = request.user.student  
        except User.student.RelatedObjectDoesNotExist:
            # User is logged in but does not have an associated student profile
            pass
    # Render the page for both logged-in and non-logged-in users
    return render(request, 'index.html', {'student': student})



def BSc_admission_Form(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        image = request.FILES['image']
        file = request.FILES['file']
        branch = request.POST['branch']
        father_name = request.POST['father_name']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        caste = request.POST['caste']
        mobile = request.POST['mobile']
        email = request.POST['email']
        adhar = request.FILES['adhar']

        admission_form = BSc_Admission_Form.objects.create(fullname=fullname, image=image,file=file,branch=branch, father_name=father_name,
                                                       date_of_birth=date_of_birth,
                                                       gender=gender, caste=caste, mobile=mobile, email=email, adhar=adhar)

        admission_form.save()

        context = {
            'fullname': fullname,
            'image': image,
            'file': file,
            'branch': branch,
            'father_name': father_name,
            'date_of_birth': date_of_birth,
            'gender': gender,
            'caste': caste,
            'mobile': mobile,
            'email': email,
            'adhar': adhar
        }



        messages.success(request,
                         'your admission form has been successfully submitted....wait for reply messege it takes some working days')

        return render(request, 'home/BSc_admission_form_confirmation.html', context)

    return render(request, 'home/addmission_form.html')

def download_confirmation(request):  
    return render(request, 'home/BSc_admission_form_confirmation.html')


def tabledata(request):
    Data1 = BSc_Admission_Form.objects.all()
    Data2 = {
        'data1': Data1
    }
    return render(request, 'home/home3.html', Data2)



def signup_view(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request,'Logged in successfully')
            return redirect('index') 
    else:
        form = StudentSignUpForm()
    

    return render(request, 'auth/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'Logged in successfully')
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


@login_required
def results_view(request):
    student = request.user  # Fetch the logged-in user
    results = Result.objects.filter(student=student)  # Fetch results for this student
    return render(request, 'students/results.html', {'student': student, 'results': results})


def ug_course_details(request,course_name):
    course = get_object_or_404(UG_Course,name = course_name)
    return render(request,'home/ug_course_details.html',{'course':course})

def time_table(request):
    return render(request,'students/time_table.html')

def UG_Studys(request):
    papers = UG_Study.objects.all()
    return render(request,'students/ug_papers.html',{'papers':papers})

def contact(request):
    return render(request,'contact.html')

def gallery_view(request):
    images = Gallery.objects.all()
    return render(request,'gallery.html',{'images':images})

def about2(request):
    return render(request,'about2.html')

def notification_view(request):
    name = Notification.objects.all()
    return render(request,'notification.html',{'names':name})


def working(request):
    return HttpResponse("Sorr For The Inconvenience.... Currently Working On That")