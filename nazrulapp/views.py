from django.shortcuts import render,redirect
from nazrulapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerPage(req):
    if req.method == 'POST':
        r_username = req.POST.get('username')
        r_email = req.POST.get('email')
        r_phone = req.POST.get('phone')
        r_nid = req.POST.get('nid')
        r_password = req.POST.get('password')
        r_confirm_password = req.POST.get('confirm_password')


        user_exist = UserModel.objects.filter(username=r_username).exists()
        email_exist = UserModel.objects.filter(email=r_email).exists()

        if user_exist and email_exist:
            messages.error(req,'User already exist')

        else:
            if r_password == r_confirm_password:
                UserModel.objects.create_user(
                    username=r_username,
                    email=r_email,
                    password=r_password,
                    phone=r_phone,
                    nid=r_nid
                )
                messages.success(req,'Registration successfully')
                return redirect('login')
            else:
                 messages.error(req,'Password does not match')
            
    return render(req,'account/register.html')



def loginPage(req):
    if req.method == 'POST':
        l_username = req.POST.get('username')
        l_password = req.POST.get('password')

        user = authenticate(req,username=l_username,password=l_password)

        if user:
            login(req,user)
            messages.success(req,'Login successfully')
            return redirect('dashboard')
        else:
            messages.error(req,'Invalid email or password')
    return render(req,'account/login.html')

@login_required
def dashboardPage(req):
    return render(req,'page/dashboard.html')

def logoutPage(req):
    logout(req)
    messages.success(req,'Logout successfully')
    return redirect('login')
        

@login_required
def doctorPage(req):
    if req.method == 'POST':
        d_name = req.POST.get('name')
        d_specialization = req.POST.get('specialization')
        d_mobile = req.POST.get('mobile')
        d_address = req.POST.get('address')
        d_email = req.POST.get('email')

        DoctorModel.objects.create(
            name=d_name,
            specialization=d_specialization,
            mobile=d_mobile,
            address=d_address,
            email=d_email
        )

        messages.success(req,'Doctor added successfully')

    data = DoctorModel.objects.all()

    context = {
        'doctors':data
    }

    return render(req,'page/doctor.html',context)


@login_required
def patientPage(req):
    if req.method == 'POST':
        p_name = req.POST.get('name')
        p_phone = req.POST.get('phone')
        p_address = req.POST.get('address')

        PatientModel.objects.create(
            name=p_name,
            phone=p_phone,
            address=p_address
        )

        messages.success(req,'Patient added successfully')

    data = PatientModel.objects.all()

    context = {
        'patients':data
    }

    return render(req,'page/patient.html',context)

@login_required
def editPage(req,id):
    data = DoctorModel.objects.get(id=id)

    if req.method == 'POST':
        d_name = req.POST.get('name')
        d_specialization = req.POST.get('specialization')
        d_mobile = req.POST.get('mobile')
        d_address = req.POST.get('address')
        d_email = req.POST.get('email')

        DoctorModel.objects.filter(id=id).update(
            name=d_name,
            specialization=d_specialization,
            mobile=d_mobile,
            address=d_address,
            email=d_email
        )

        messages.success(req,'Doctor edited successfully')
        return redirect('doctor')

    context = {
        'doctor':data
    }

    return render(req,'page/doctor.html',context)

@login_required
def deletePage(req,id):
    DoctorModel.objects.get(id=id).delete()
    messages.success(req,'Doctor deleted successfully')
    return redirect('doctor')
