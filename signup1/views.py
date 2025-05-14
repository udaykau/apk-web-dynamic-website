from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Registration, contact, Campaign,Credit_Card_Banking, Life_Insurance,Health_Insurance, Motor_Insurance, Capping, Form_Campaign, APKEducation, SecureCare, Fire_Insurance, Liability_Insurance, Marine_Insurance, A_H_Insurance, Credit_Card, Credit_Card_Bank, complaint
from apkshopee.models import Billing_Address
from django.contrib.auth import authenticate, login, logout
import math, random
import datetime
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from requests.packages import urllib3
import requests
from itertools import chain
from django.core.mail import send_mail
urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'

def Index(request):
    if request.method == 'POST':
        text = request.POST['mail']
        if Registration.objects.filter(email=text).exists() or Registration.objects.filter(phone=text).exists():
            digits = "0123456789"
            OTP = ""
            for i in range(4):
                OTP += digits[math.floor(random.random() * 10)]
            if text.isdigit():
                temp = "https://japi.instaalerts.zone/httpapi/QueryStringReceiver?ver=1.0&key=nJvr3Fb6GCWlwzVbTkjvaA==&encrpt=0&dest="+ text +"&send=APKWEB&text=Your%20One%20Time%20Password%20for%20APK%20is%20" + OTP
                r = requests.get(temp, verify=False)
                username = str(OTP)+text
            else:
                send_mail(
                    'APKWEB AGGREGATOR OTP Verification',
                    'Thank you, For Registering in APKWEB AGGREGATOR your OTP is ' + OTP,
                    'info@apkweb.in',
                    [text],
                    fail_silently=False,
                )
                username = str(OTP)+text
            return render(request, 'otp.html', {'username': username})
        else:
            messages.error(request, "No User Found Try Again...")
            return redirect('Login')
    return render(request, 'index/index.html')


def Login(request):
    if request.method == 'POST':
        login_email = request.POST['username']
        login_password = request.POST['pass']
        user = authenticate(username=login_email, password=login_password)
        if Registration.objects.filter(email=login_email).exists() and user is not None:
            login(request, user)
            return redirect('Dashboard')
        else:
            messages.error(request, "Try Again: Incorrect Username or password")
            return redirect('Login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST' or request.FILES:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        pin = request.POST['Pin Code']
        password = request.POST['password']
        re_password = request.POST['re_password']
        if password != re_password:
            messages.error(request, "Enter Password Doesn't match. Try Again...")
            return redirect('register')
        if len(password) < 6:
            messages.error(request, "Entered Password is weak. Try Again...")
            return redirect('register')
        if len(phone) < 10 or len(phone) > 10:
            messages.error(request, "Incorrect Phone No. Try Again...")
            return redirect('register')
        if len(name) < 4:
            messages.error(request, "Use Valid Name. Try Again...")
            return redirect('register')
        if Registration.objects.filter(email = email).exists():
            messages.error(request, "User Already Exist...")
            return redirect('Login')
        data = Registration(name=name, email=email, phone=phone, Pan_No=address, Pin_Code=pin)
        data.save()
        user = User.objects.create_user(username=email, password=password)
        user.is_active = False
        digits = "0123456789"
        OTP = ""
        for i in range(4):
            OTP += digits[math.floor(random.random() * 10)]
        temp = "https://japi.instaalerts.zone/httpapi/QueryStringReceiver?ver=1.0&key=nJvr3Fb6GCWlwzVbTkjvaA==&encrpt=0&dest="+ phone +"&send=APKWEB&text=Thanks%20for%20registering%20with%20APK.%20Your%20OTP%20is%20" + OTP
        r = requests.get(temp, verify=False)
        send_mail(
            'APKWEB AGGREGATOR OTP Verification',
            'Thank you, For Registering in APKWEB AGGREGATOR your OTP is ' + OTP +'\n\nUsername: '+ email +'\nPassword: '+ password,
            'from@example.com',
            [email],
            fail_silently=False,
        )
        mail = str(OTP)+email
        user.save()
        return render(request, 'register_otp.html', {'username': mail})
    return render(request, 'register.html')


def otp(request):
    if request.method == "POST":
        access = request.POST['secure']
        username = request.POST['username']
        if access == username[:4]:
            return render(request, 'newpassword.html', {'email': username[4:]})
        else:
            messages.error(request, "Wrong OTP Try Again...")
            return render(request, 'otp.html', {'username': username})


def register_otp(request):
    if request.method == "POST":
        access = request.POST['secure']
        email = request.POST['username']
        if access == email[:4]:
            user = User.objects.get(username= email[4:])
            user.is_active = True
            user.save()
            return render(request, 'login.html')
        else:
            messages.error(request, "Wrong OTP Try Again...")
            return render(request, 'register_otp.html', {'username': email})


def new_password(request):
    if request.method == "POST":
        email= request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        if password != re_password:
            messages.error(request, "Enter Password Doesn't match. Try Again...")
            return redirect('new_password')
        if len(password) < 6:
            messages.error(request, "Entered Password is weak. Try Again...")
            return redirect('new_password')
        user = User.objects.get(username= email)
        user.set_password(password)
        user.save()
        messages.success(request, "Password Changed Successfully...")
        return redirect('Login')
    return render(request, 'newpassword.html')

@login_required
def Dashboard(request):
    username = request.user.username
    wallet1 = Capping.objects.filter(User_Email=username)
    wallet2 = Life_Insurance.objects.filter(Merchant_mail=username)
    wallet3 = Health_Insurance.objects.filter(Merchant_mail=username)
    wallet4 = Motor_Insurance.objects.filter(Merchant_mail=username)
    wallet5 = Fire_Insurance.objects.filter(Merchant=username)
    wallet6 = Liability_Insurance.objects.filter(Merchant=username)
    wallet7 = Marine_Insurance.objects.filter(Merchant=username)
    wallet8 = A_H_Insurance.objects.filter(Merchant=username)
    wallet9 = SecureCare.objects.filter(Merchant_mail=username)
    wallet10 = Credit_Card.objects.filter(Merchant_mail=username)
    wallet11 = Billing_Address.objects.filter(Merchant_mail = username)
    points = 0
    Pending_Points = 0
    for w in wallet1:
        points += int(w.Points)
        Pending_Points += int(w.Pending_Points)
    for w in wallet10:
        points += int(w.Points)
    for w in wallet2:
        if w.Commission.isdigit():
            points += int(w.Commission)
    for w in wallet3:
        if w.Commission.isdigit():
            points += int(w.Commission)
    for w in wallet4:
        if w.Commission.isdigit():
            points += int(w.Commission)
    for w in wallet5:
        if w.Commission.isdigit():
            points += int(w.Commission)
    for w in wallet6:
        if w.Commission.isdigit():
            points += int(w.Commission)
    for w in wallet7:
        if w.Commission.isdigit():
            points += int(w.Commission)
    for w in wallet8:
        if w.Commission.isdigit():
            points += int(w.Commission)
    for w in wallet9:
        if w.Commission.isdigit():
            points += int(w.Commission)
    for w in wallet11:
        points -= int(w.Total_Price.replace(',', ''))
    register = Registration.objects.get(email = username)
    register.Points = points
    register.Pending_Points = Pending_Points
    register.save()
    return render(request, 'dashboard.html', {'wallet': points})


@login_required
def carry99(request):
    return render(request, 'Carry99/index.html')


@login_required
def kisan_shakti_kendra(request):
    return render(request, 'ksk/index.html')


@login_required
def mobileperks(request):
    return render(request, 'Mobileperks/index.html')


@login_required
def Contact(request):
    username = request.user.username
    register = Registration.objects.get(email=username)
    total = register.Points
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_detail = contact(first_name=first_name, last_name=last_name, email=email, subject=subject, message=message)
        contact_detail.save()
        messages.success(request, "Our Team Will Contact You Shortly...")
        return redirect('Dashboard')
    return render(request, 'contact.html', {'wallet': total})


@login_required
def Complaint(request):
    username = request.user.username
    register = Registration.objects.get(email=username)
    total = register.Points
    if request.method == 'POST':
        Name = request.POST['name']
        ID = request.POST['ID']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['complaint']
        complaints = complaint(Name=Name, User_ID = ID, email=email, phone=phone, subject=subject, message=message)
        complaints.save()
        send_mail(
            'Feedback Confirmation',
            'Your complaint has been registered successfully. \nWe have received your feedback and will contact you shortly regarding the same.\nThanks & Regards',
            'from@example.com',
            [email],
            fail_silently=True,
        )
        send_mail(
            'Complaint APKWEB',
            'ID: '+ID +'\nNAME: '+ Name +'\nEmail'+ email +'\nPhone'+phone +'\nSUBJECT: '+ subject +'MESSAGE: '+message,
            'from@example.com',
            ['apkwebaggregator@gmail.com'],
            fail_silently=True,
        )
        messages.success(request, "Our Team Will Contact You Shortly...")
        return redirect('Dashboard')
    return render(request, 'Complaint.html', {'wallet': total, 'user': register})


@login_required
def onlineCampaign(request):
    username = request.user.username
    register = Registration.objects.get(email=username)
    total = register.Points
    campaigns = Campaign.objects.filter(Active=True)
    data = {"campaigns": campaigns, 'wallet': total}
    return render(request, 'online campaigns.html', data)


@login_required
def campaign(request, sno):
    username = request.user.username
    register = Registration.objects.get(email=username)
    total = register.Points
    id = Campaign.objects.get(sno = sno)
    terms_and_condition = id.Terms_and_condition.split(';')
    do = id.Does.split(';')
    dont = id.Dont.split(';')
    data = {"campaign": id, 'does': do, 'donts':dont, 'wallet': total, 'terms_and_condition' : terms_and_condition}
    if request.method == 'POST':
        detail = request.POST['send']
        if Capping.objects.filter(User_Email=username, Campaign_Sno=str(sno)).exists():
            today = datetime.date.today()
            datas = Capping.objects.filter(Campaign_Sno=str(sno), User_Email=username)
            count = 0
            for data2 in datas:
                if today.day == data2.date.day and today.month == data2.date.month and today.year == data2.date.year:
                    if data2.capping <= 0:
                        messages.error(request, "Your Capping is Full Try another Campaign...")
                        return render(request, 'campaign.html', data)
                    data2.Pending_Points = data2.Pending_Points + data2.Points
                    data2.Detail = detail + ',' + data2.Detail
                    data2.capping = data2.capping - 1
                    data2.save()
                    count = 1
            if count == 0:
                cap = id.Capping - 1
                data2 = Capping(Campaign_Sno=sno, Campaign_Name=id.Campaign_Name, capping=cap, User_Email=username,Detail=detail, Pending_Points=id.points)
                data2.save()
        else:
            cap = id.Capping - 1
            data2 = Capping(Campaign_Sno=sno, Campaign_Name=id.Campaign_Name, capping=cap, User_Email=username, Detail=detail, Pending_Points=id.points)
            data2.save()
        data3 = Registration.objects.get(email=username)
        data1 = Form_Campaign(User_Email=username, Campaign_Sno=sno, Send_on=detail, Campaign_Name = id.Campaign_Name)
        data1.save()
        if detail.isdigit():
            link = repr(id.Link).format(data1.sno, data3.sno, detail)
            temp = "https://japi.instaalerts.zone/httpapi/QueryStringReceiver?ver=1.0&key=nJvr3Fb6GCWlwzVbTkjvaA==&encrpt=0&dest="+ detail +"&send=APKWEB&text=To%20complete%20the%20task%20please%20click%20on%20the%20given%20link%20"+link
            r = requests.get(temp, verify=False)
        else:
            if id.Mail_body:
                subject = id.Mail_Subject
                body = id.Mail_Content
                link = id.Link_Email.format(data1.sno, data3.sno, detail)
                send_mail(
                    subject,
                     body+'\n\n'+link,
                    'from@example.com',
                    [detail],
                    fail_silently=True,
                )
            else:
                link = id.Link_Email.format(data1.sno, data3.sno, detail)
                send_mail(
                    'APKWEB AGGREGATOR Campaign Link',
                    'Thank You For Your Interest in our Online Campaign Click this link below\n\n' + link,
                    'from@example.com',
                    [detail],
                    fail_silently=True,
                )
        messages.error(request, "Send Successfully "+"Capping :" + str(data2.capping) + " Available For You")
        return render(request, 'campaign.html', data)
    return render(request, 'campaign.html', data)


@login_required
def coming_soon(request):
    return render(request, 'coming soon.html')


@login_required
def Life_insurance(request):
    if request.method == 'POST':
        experience = request.POST['experience']
        nationality = request.POST['nationality']
        self = request.POST['self']
        adhaar_number = request.POST['adhaar_number']
        pan_no = request.POST['pan_no']
        mobile = request.POST['mobile']
        email = request.POST['email']
        mname = request.POST['mname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        house_no = request.POST['house_no']
        area = request.POST['area']
        town = request.POST['town']
        Landmark = request.POST['Landmark']
        Country = request.POST['Country']
        State = request.POST['State']
        City = request.POST['City']
        pincode = request.POST['pincode']
        altmobile = request.POST['altmobile']
        addressproof = request.POST['addressproof']
        addressproofno = request.POST['addressproofno']
        addproofimgf = request.FILES.get('addproofimgf')
        addproofimgr = request.FILES.get('addproofimgr')
        pan_image = request.FILES.get('pan_image')
        photo = request.FILES.get('photo')
        username = request.user.username
        data = Life_Insurance(Merchant_mail=username, First_Name=fname, Middle_Name=mname, Last_Name=lname, DOB = dob, Adhaar_number=adhaar_number, Pan_No=pan_no,
                                         Mobile=mobile, Email=email, House_No=house_no, Area=area, Town=town, Landmark=Landmark, Country=Country,
                                         State=State, City=City, Pin_code=pincode, Alt_mobile=altmobile, Address_proof=addressproof, Address_Proof_No=addressproofno,
                                         Pan_Card=pan_image, Photo=photo, Address_Proof_img_front=addproofimgf, Address_Proof_img_Back=addproofimgr,
                                    Experience=experience, Nationality=nationality, Self=self)
        data.save()
        send_mail(
            'Application Form Submission',
            'Hello Sir,Your application has been submitted successfully with application ID:' + data.sno +'\nKindly save the Application Number for future reference.\nThanks & Regards',
            'from@example.com',
            [mobile],
            fail_silently=True,
        )
        messages.error(request, "Saved Successfully")
        return redirect('Dashboard')
    return render(request, 'max form/life/formpage.html')


@login_required
def Motor_insurance(request):
    if request.method == 'POST':
        veh_name = request.POST['veh_name']
        veh_year = request.POST['veh_year']
        veh_reg = request.POST['veh_reg']
        veh_engine = request.POST['veh_engine']
        Veh_chasis = request.POST['Veh_chasis']
        rc_image = request.FILES.get('rc_image')
        pre_insurance = request.FILES.get('pre_insurance')
        username = request.user.username
        data = Motor_Insurance(Merchant_mail=username, Vehicle_Name=veh_name, Vehicle_Year=veh_year, Vehicle_Registration_No=veh_reg, Vehicle_engine=veh_engine, Vehicle_Chasis=Veh_chasis, RC_Image=rc_image,
                                         Pre_Insurance=pre_insurance)
        data.save()
        messages.error(request, "Saved Successfully")
        return redirect('Dashboard')
    return render(request, 'max form/motor/formpage.html')


@login_required
def Health_insurance(request):
    if request.method == 'POST':
        experience = request.POST['experience']
        nationality = request.POST['nationality']
        self = request.POST['self']
        adhaar_number = request.POST['adhaar_number']
        pan_no = request.POST['pan_no']
        mobile = request.POST['mobile']
        email = request.POST['email']
        mname = request.POST['mname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        house_no = request.POST['house_no']
        area = request.POST['area']
        town = request.POST['town']
        Landmark = request.POST['Landmark']
        Country = request.POST['Country']
        State = request.POST['State']
        City = request.POST['City']
        pincode = request.POST['pincode']
        altmobile = request.POST['altmobile']
        addressproof = request.POST['addressproof']
        addressproofno = request.POST['addressproofno']
        addproofimgf = request.FILES.get('addproofimgf')
        addproofimgr = request.FILES.get('addproofimgr')
        pan_image = request.FILES.get('pan_image')
        photo = request.FILES.get('photo')
        username = request.user.username
        data = Health_Insurance(Merchant_mail=username, First_Name=fname, Middle_Name=mname, Last_Name=lname, DOB = dob, Adhaar_number=adhaar_number, Pan_No=pan_no,
                                         Mobile=mobile, Email=email, House_No=house_no, Area=area, Town=town, Landmark=Landmark, Country=Country,
                                         State=State, City=City, Pin_code=pincode, Alt_mobile=altmobile, Address_proof=addressproof, Address_Proof_No=addressproofno,
                                         Pan_Card=pan_image, Photo=photo, Address_Proof_img_front=addproofimgf, Address_Proof_img_Back=addproofimgr,
                                    Experience=experience, Nationality=nationality, Self=self)
        data.save()
        send_mail(
            'Application Form Submission',
            'Hello Sir,Your application has been submitted successfully with application ID:' + data.sno + '\nKindly save the Application Number for future reference.\nThanks & Regards',
            'from@example.com',
            [mobile],
            fail_silently=True,
        )
        messages.error(request, "Saved Successfully")
        return redirect('Dashboard')
    return render(request, 'max form/health/formpage.html')


@login_required
def Fire_insurance(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        company = request.POST['companyname']
        email = request.POST['email']
        username = request.user.username
        data = Fire_Insurance(Name= name,Merchant= username, Mobile= mobile, Organization_Name=company, Email=email)
        data.save()
        send_mail(
            'Application Form Submission',
            'Hello Sir,Your application has been submitted successfully with application ID:' + data.sno + '\nKindly save the Application Number for future reference.\nThanks & Regards',
            'from@example.com',
            [mobile],
            fail_silently=True,
        )
        messages.error(request, "Saved Successfully")
        return redirect('Dashboard')
    return render(request, 'max form/fire/formpage.html')


@login_required
def Liability_insurance(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        company = request.POST['companyname']
        email = request.POST['email']
        city = request.POST['city']
        username = request.user.username
        data = Liability_Insurance(Name= name,Merchant= username,City=city, Mobile= mobile, Organization_Name=company, Email=email)
        data.save()
        send_mail(
            'Application Form Submission',
            'Hello Sir,Your application has been submitted successfully with application ID:' + data.sno + '\nKindly save the Application Number for future reference.\nThanks & Regards',
            'from@example.com',
            [mobile],
            fail_silently=True,
        )
        messages.error(request, "Saved Successfully")
        return redirect('Dashboard')
    return render(request, 'max form/liability/formpage.html')


@login_required
def Marine_insurance(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        company = request.POST['companyname']
        email = request.POST['email']
        username = request.user.username
        data = Marine_Insurance(Name= name,Merchant= username, Mobile= mobile, Organization_Name=company, Email=email)
        data.save()
        send_mail(
            'Application Form Submission',
            'Hello Sir,Your application has been submitted successfully with application ID:' + data.sno + '\nKindly save the Application Number for future reference.\nThanks & Regards',
            'from@example.com',
            [mobile],
            fail_silently=True,
        )
        messages.error(request, "Saved Successfully")
        return redirect('Dashboard')
    return render(request, 'max form/marine/formpage.html')


@login_required
def AH_insurance(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        company = request.POST['companyname']
        email = request.POST['email']
        username = request.user.username
        data = A_H_Insurance(Name= name,Merchant= username, Mobile= mobile, Organization_Name=company, Email=email)
        data.save()
        send_mail(
            'Application Form Submission',
            'Hello Sir,Your application has been submitted successfully with application ID:' + data.sno + '\nKindly save the Application Number for future reference.\nThanks & Regards',
            'from@example.com',
            [mobile],
            fail_silently=True,
        )
        messages.error(request, "Saved Successfully")
        return redirect('Dashboard')
    return render(request, 'max form/AandH/formpage.html')


@login_required
def verify_detail(request):
    if request.method == "POST":
        access = request.POST['secure']
        username = request.POST['username']
        if access == username[:4]:
            data2 = SecureCare.objects.get(Email=username[4:])
            data2.Verified = True
            data2.save()
            messages.error(request, "Verified Successfully")
            return redirect('Dashboard')
        else:
            messages.error(request, "Wrong OTP Try Again...")
            return render(request, 'verify.html', {'username': username})
    return render(request, 'verify.html')


@login_required
def securecare(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        address = request.POST['address']
        mobile = request.POST['mobile']
        email = request.POST['email']
        job = request.POST.getlist('job')
        addproofimgf = request.FILES.get('addproofimgf')
        addproofimgr = request.FILES.get('addproofimgr')
        pan_image = request.FILES.get('pan_image')
        photo = request.FILES.get('photo')
        if SecureCare.objects.filter(Email=email).exists() or SecureCare.objects.filter(Mobile= mobile).exists():
            messages.error(request, 'Email or Phone Number already Exist')
            return redirect('securecare')
        username = request.user.username
        data = SecureCare(Merchant_mail=username, First_Name=fname, Middle_Name=mname, Last_Name=lname, Address = address,
                                   Mobile=mobile, Email=email,Job_Detail=job, Pan_Card=pan_image, Photo=photo, Address_Proof_img_front=addproofimgf, Address_Proof_img_Back=addproofimgr)
        data.save()
        digits = "0123456789"
        OTP = ""
        for i in range(4):
            OTP += digits[math.floor(random.random() * 10)]
        temp = "https://japi.instaalerts.zone/httpapi/QueryStringReceiver?ver=1.0&key=nJvr3Fb6GCWlwzVbTkjvaA==&encrpt=0&dest=" + mobile + "&send=APKWEB&text=Your%20One%20Time%20Password%20for%20APK%20is%20" + OTP
        r = requests.get(temp, verify=False)
        username = str(OTP) + email
        return render(request, 'verify.html', {'username': username})
    return render(request, 'secure/formpage.html')


@login_required
def verify_details(request):
    if request.method == "POST":
        access = request.POST['secure']
        username = request.POST['username']
        if access == username[:4]:
            data2 = APKEducation.objects.get(Email=username[4:])
            data2.Verified = True
            data2.save()
            messages.error(request, "Verified Successfully")
            return redirect('Dashboard')
        else:
            messages.error(request, "Wrong OTP Try Again...")
            return render(request, 'verify1.html', {'username': username})
    return render(request, 'verify1.html')


@login_required
def apkeducation(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        address = request.POST['Aadress']
        mobile = request.POST['mobile']
        email = request.POST['email']
        addproofimgf = request.FILES.get('addproofimgf')
        addproofimgr = request.FILES.get('addproofimgr')
        pan_image = request.FILES.get('pan_image')
        photo = request.FILES.get('photo')
        if APKEducation.objects.filter(Email=email).exists() or APKEducation.objects.filter(Mobile= mobile).exists():
            messages.error(request, 'Email or Phone Number already Exist')
            return redirect('apkeducation')
        username = request.user.username
        data = APKEducation(Merchant_mail=username, First_Name=fname, Middle_Name=mname, Last_Name=lname, Address = address,
                                   Mobile=mobile, Email=email, Pan_Card=pan_image, Photo=photo, Address_Proof_img_front=addproofimgf, Address_Proof_img_Back=addproofimgr)
        data.save()
        digits = "0123456789"
        OTP = ""
        for i in range(4):
            OTP += digits[math.floor(random.random() * 10)]
        temp = "https://japi.instaalerts.zone/httpapi/QueryStringReceiver?ver=1.0&key=nJvr3Fb6GCWlwzVbTkjvaA==&encrpt=0&dest=" + mobile + "&send=APKWEB&text=Your%20One%20Time%20Password%20for%20APK%20is%20" + OTP
        r = requests.get(temp, verify=False)
        username = str(OTP) + email
        return render(request, 'verify1.html', {'username': username})
    return render(request, 'apkeducation/formpage.html')

@login_required
def form(request):
    return render(request, 'formpage.html')


@login_required
def about(request):
    username = request.user.username
    register = Registration.objects.get(email=username)
    total = register.Points
    return render(request, 'about.html', {'wallet': total})


@login_required
def campaign_form(request):
    username = request.user.username
    register = Registration.objects.get(email=username)
    total = register.Points
    return render(request, 'campaign form.html', {'wallet': total})


@login_required
def report(request, date):
    username = request.user.username
    insurance1 = Life_Insurance.objects.filter(Merchant_mail=username)
    insurance2 = Health_Insurance.objects.filter(Merchant_mail=username)
    insurance3 = Motor_Insurance.objects.filter(Merchant_mail=username)
    insurances = list(chain(insurance2, insurance1, insurance3))
    campaign = Form_Campaign.objects.filter(User_Email=username)
    secures = SecureCare.objects.filter(Merchant_mail=username)
    credits = Credit_Card.objects.filter(Merchant_mail=username)
    today = datetime.date.today()
    campaigns = []
    credit = []
    secure = []
    insurance = []
    if date == 'Daily_report':
        for i in campaign:
            if today.day == i.date.day and today.month == i.date.month and today.year == i.date.year:
                campaigns.append(i)
        for i in credits:
            if today.day == i.date.day and today.month == i.date.month and today.year == i.date.year:
                credit.append(i)
        for i in secures:
            if today.day == i.date.day and today.month == i.date.month and today.year == i.date.year:
                secure.append(i)
        for i in insurances:
            if today.day == i.date.day and today.month == i.date.month and today.year == i.date.year:
                insurance.append(i)
    elif date == 'Weekly_report':
        for i in campaign:
            if i.date.date() >= today - timedelta(weeks=1):
                campaigns.append(i)
        for i in credits:
            if i.date.date() >= today - timedelta(weeks=1):
                credit.append(i)
        for i in secures:
            if i.date.date() >= today - timedelta(weeks=1):
                secure.append(i)
        for i in insurances:
            if i.date.date() >= today - timedelta(weeks=1):
                insurance.append(i)
    elif date == 'Monthly_report':
        for i in campaign:
            if  i.date.date() >= today - timedelta(weeks=4):
                campaigns.append(i)
        for i in credits:
            if i.date.date() >= today - timedelta(weeks=4):
                credit.append(i)
        for i in secures:
            if i.date.date() >= today - timedelta(weeks=4):
                secure.append(i)
        for i in insurances:
            if i.date.date() >= today - timedelta(weeks=4):
                insurance.append(i)
    else:
        campaigns = campaign
        credit = credits
        secure = secures
        insurance = insurances
    return render(request, 'report/index.html', {'campaign':campaigns, 'Secure':secure, 'Creditcard': credit, 'insurance': insurance})


@login_required
def credit_card(request):
    username = request.user.username
    data = Credit_Card.objects.filter(Merchant_mail=username)
    list = Credit_Card_Banking.objects.filter(Active=True)
    return render(request, 'credit_card/index2.html', {'data': data, 'list': list})




@login_required
def CreditCard(request):
    banks = Credit_Card_Bank.objects.filter(Active=True)
    if request.method == 'POST':
        Bank = request.POST['bank']
        pincode = request.POST['pincode']
        customer_name = request.POST['customer_name']
        contact = request.POST['contact']
        ALT_Number = request.POST['ALT_Number']
        app_number = request.POST['app_number']
        AGENT_Name = request.POST['AGENT_Name']
        email = request.POST['email']
        surrogate = request.POST['surrogate']
        Salary = request.POST['Salary']
        pan_card = request.POST['pan_card']
        card_copy = request.FILES.get('card_copy')
        Salary_slip = request.FILES.get('Salary_slip')
        kyc = request.FILES.get('kyc')
        photo = request.FILES.get('photo')
        id_card = request.FILES.get('id_card')
        username = request.user.username
        data = Credit_Card(Merchant_mail=username, Bank_Name=Bank, Pin_Code=pincode, Customer_Name=customer_name, Contact=contact,
                          ALT_Number=ALT_Number, Form_Application_Number=app_number, AGENT_Name=AGENT_Name, Customer_Email=email, Bank_Surrogate=surrogate,
                          Customer_Limit_Salary=Salary, Pan_Card=pan_card, Card_Copy=card_copy, Salary_Slip=Salary_slip, KYC=kyc, Photo=photo, Official_ID_Card=id_card)
        data.save()
        send_mail(
            'Application Form Submission',
            'Hello Sir,Your application has been submitted successfully with application ID:' + data.sno + '\nKindly save the Application Number for future reference.\nThanks & Regards',
            'from@example.com',
            [email],
            fail_silently=True,
        )
    return render(request, 'credit_card/formpage.html', {'bank': banks})


@login_required
def account_opening(request):
    list = Credit_Card_Banking.objects.filter(Active=True)
    for id in list:
        terms_and_condition = id.fresh_card.split(',')
        do = id.Dcouments.split(',')
        dont = id.Bank_CardToCard.split(',')
    return render(request, 'account opening/index.html')


@login_required
def insurance(request):
    username = request.user.username
    register = Registration.objects.get(email=username)
    total = register.Points
    return render(request, 'insurance.html', {'wallet': total})


@login_required
def logout_user(request):
    logout(request)
    return redirect('Login')
