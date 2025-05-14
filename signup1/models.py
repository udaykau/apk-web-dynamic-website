from django.db import models
from datetime import datetime
import os


def get_upload_path(instance, filename):
    os.path.join('media/', instance.email)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dire = '{0}/{1}'.format(instance.email, filename)
    return str(dire)


class Registration(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    Pan_No = models.CharField(max_length=100)
    Pin_Code = models.CharField(max_length=20)
    Pending_Points = models.IntegerField(default=0)
    Points = models.IntegerField(default=0)
    Pan_card = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    aadhar_card = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    Cancelled_Cheque = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    Photo = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' ' + self.Pin_Code


# Create your models here.
class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=3000)
    date = models.DateTimeField(auto_now=True)


# Create your models here.
class complaint(models.Model):
    sno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    User_ID = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=3000)
    date = models.DateTimeField(auto_now=True)


def get_upload_pathe(instance, filename):
    os.path.join('media/Max_insurance/life_health/', instance.Email)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dire = '{0}/{1}'.format(instance.Email, filename)
    return str(dire)


class Life_Insurance(models.Model):
    sno = models.AutoField(primary_key=True)
    Merchant_mail = models.CharField(max_length=300)
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(blank=True, null=True, max_length=100)
    Last_Name = models.CharField(max_length=100)
    DOB = models.CharField(max_length=100)
    Experience = models.CharField(max_length=100)
    Nationality = models.CharField(max_length=100)
    Self = models.CharField(max_length=30)
    Adhaar_number = models.CharField(max_length=30)
    Pan_No = models.CharField(max_length=30)
    Mobile = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    House_No = models.CharField(max_length=30)
    Area = models.CharField(max_length=30)
    Town = models.CharField(null=True, blank=True, max_length=30)
    Landmark = models.CharField(null=True, blank=True, max_length=30)
    Country = models.CharField(max_length=30)
    State = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Pin_code = models.CharField(max_length=30)
    Alt_mobile = models.CharField(null=True, blank=True, max_length=30)
    Address_proof = models.CharField(max_length=30)
    Address_Proof_No = models.CharField(max_length=40)
    Address_Proof_img_front = models.ImageField(upload_to=get_upload_pathe)
    Address_Proof_img_Back = models.ImageField(upload_to=get_upload_pathe)
    Pan_Card = models.ImageField(upload_to=get_upload_pathe)
    Photo = models.ImageField(upload_to=get_upload_pathe)
    Cover_Status = models.CharField(max_length=500, null=True, default='In Process')
    Company = models.CharField(max_length=500, null=True, default='-')
    Policy_Issue_Date = models.DateTimeField(null=True, blank=True)
    premium_Paid = models.CharField(max_length=500, null=True, default='-')
    Commission = models.CharField(max_length=100, null=True, default='-')
    date = models.DateTimeField(auto_now=True)


class Health_Insurance(models.Model):
    sno = models.AutoField(primary_key=True)
    Merchant_mail = models.CharField(max_length=300)
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(blank=True, null=True, max_length=100)
    Last_Name = models.CharField(max_length=100)
    DOB = models.CharField(max_length=100)
    Experience = models.CharField(max_length=100)
    Nationality = models.CharField(max_length=100)
    Self = models.CharField(max_length=30)
    Adhaar_number = models.CharField(max_length=30)
    Pan_No = models.CharField(max_length=30)
    Mobile = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    House_No = models.CharField(max_length=30)
    Area = models.CharField(max_length=30)
    Town = models.CharField(null=True, blank=True, max_length=30)
    Landmark = models.CharField(null=True, blank=True, max_length=30)
    Country = models.CharField(max_length=30)
    State = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Pin_code = models.CharField(max_length=30)
    Alt_mobile = models.CharField(null=True, blank=True, max_length=30)
    Address_proof = models.CharField(max_length=30)
    Address_Proof_No = models.CharField(max_length=40)
    Address_Proof_img_front = models.ImageField(upload_to=get_upload_pathe)
    Address_Proof_img_Back = models.ImageField(upload_to=get_upload_pathe)
    Pan_Card = models.ImageField(upload_to=get_upload_pathe)
    Photo = models.ImageField(upload_to=get_upload_pathe)
    Cover_Status = models.CharField(max_length=500, null=True, default='In Process')
    Company = models.CharField(max_length=500, null=True, default='-')
    Policy_Issue_Date = models.DateTimeField(null=True, blank=True)
    premium_Paid = models.CharField(max_length=500, null=True, default='-')
    Commission = models.CharField(max_length=100, null=True, default='-')
    date = models.DateTimeField(auto_now=True)



def get_upload_pathee(instance, filename):
    os.path.join('media/Max_insurance/Motor/', instance.Email)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dire = '{0}/{1}'.format(instance.Email, filename)
    return str(dire)


class Motor_Insurance(models.Model):
    sno = models.AutoField(primary_key=True)
    Merchant_mail = models.CharField(max_length=300)
    Vehicle_Name = models.CharField(max_length=30)
    Vehicle_Year = models.CharField(max_length=100)
    Vehicle_Registration_No = models.CharField(max_length=100)
    Vehicle_engine = models.CharField(max_length=30)
    Vehicle_Chasis = models.CharField(max_length=30)
    RC_Image = models.ImageField(upload_to=get_upload_pathee)
    Pre_Insurance = models.ImageField(upload_to=get_upload_pathee)
    Cover_Status = models.CharField(max_length=500, null=True, default='In Process')
    Company = models.CharField(max_length=500, null=True, default='-')
    Policy_Issue_Date = models.DateTimeField(null=True, blank=True)
    premium_Paid = models.CharField(max_length=500, null=True, default='-')
    Commission = models.CharField(max_length=100, null=True, default='-')
    date = models.DateTimeField(auto_now=True)


class Fire_Insurance(models.Model):
    sno = models.AutoField(primary_key=True)
    Merchant = models.CharField(max_length=100)
    Name = models.CharField(max_length=200)
    Mobile = models.CharField(max_length=50)
    Organization_Name = models.CharField(max_length=500)
    Email = models.CharField(max_length=100)
    Cover_Status = models.CharField(max_length=500, null=True, default='In Process')
    Company = models.CharField(max_length=500, null=True, default='-')
    Policy_Issue_Date = models.DateTimeField(null=True, blank=True)
    premium_Paid = models.CharField(max_length=500, null=True, default='-')
    Commission = models.CharField(max_length=100, null=True, default='-')
    date = models.DateTimeField(auto_now=True)


class Liability_Insurance(models.Model):
    sno = models.AutoField(primary_key=True)
    Merchant = models.CharField(max_length=100)
    Name = models.CharField(max_length=200)
    Mobile = models.CharField(max_length=50)
    Organization_Name = models.CharField(max_length=500)
    Email = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Cover_Status = models.CharField(max_length=500, null=True, default='In Process')
    Company = models.CharField(max_length=500, null=True, default='-')
    Policy_Issue_Date = models.DateTimeField(null=True, blank=True)
    premium_Paid = models.CharField(max_length=500, null=True, default='-')
    Commission = models.CharField(max_length=100, null=True, default='-')
    date = models.DateTimeField(auto_now=True)


class Marine_Insurance(models.Model):
    sno = models.AutoField(primary_key=True)
    Merchant = models.CharField(max_length=100)
    Name = models.CharField(max_length=200)
    Mobile = models.CharField(max_length=50)
    Organization_Name = models.CharField(max_length=500)
    Email = models.CharField(max_length=100)
    Cover_Status = models.CharField(max_length=500, null=True, default='In Process')
    Company = models.CharField(max_length=500, null=True, default='-')
    Policy_Issue_Date = models.DateTimeField(null=True, blank=True)
    premium_Paid = models.CharField(max_length=500, null=True, default='-')
    Commission = models.CharField(max_length=100, null=True, default='-')
    date = models.DateTimeField(auto_now=True)


class A_H_Insurance(models.Model):
    sno = models.AutoField(primary_key=True)
    Merchant = models.CharField(max_length=100)
    Name = models.CharField(max_length=200)
    Mobile = models.CharField(max_length=50)
    Organization_Name = models.CharField(max_length=500)
    Email = models.CharField(max_length=100)
    Cover_Status = models.CharField(max_length=500, null=True, default='In Process')
    Company = models.CharField(max_length=500, null=True, default='-')
    Policy_Issue_Date = models.DateTimeField(null=True, blank=True)
    premium_Paid = models.CharField(max_length=500, null=True, default='-')
    Commission = models.CharField(max_length=100, null=True, default='-')
    date = models.DateTimeField(auto_now=True)


def secure_care(instance, filename):
    os.path.join('media/SecureCare', instance.Email)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dire = '{0}/{1}'.format(instance.Email, filename)
    return str(dire)


class SecureCare(models.Model):
    sno = models.AutoField(primary_key=True)
    Verified = models.BooleanField(default=False)
    Merchant_mail = models.CharField(max_length=300)
    First_Name = models.CharField(max_length=30)
    Middle_Name = models.CharField(blank=True, null=True, max_length=100)
    Last_Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Job_Detail = models.CharField(max_length=150)
    Address_Proof_img_front = models.ImageField(null=True, blank=True, upload_to=secure_care)
    Address_Proof_img_Back = models.ImageField(null=True, blank=True, upload_to=secure_care)
    Pan_Card = models.ImageField(null=True, blank=True, upload_to=secure_care)
    Photo = models.ImageField(null=True, blank=True, upload_to=secure_care)
    Salary = models.CharField(max_length=100 ,null=True, default='-')
    Commission = models.CharField(max_length=100, blank=True, default='-')
    date = models.DateTimeField(auto_now=True)


def APK_Education(instance, filename):
    os.path.join('media/APKEducation', instance.Email)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dire = '{0}/{1}'.format(instance.Email, filename)
    return str(dire)


class APKEducation(models.Model):
    sno = models.AutoField(primary_key=True)
    Verified = models.BooleanField(default=False)
    Merchant_mail = models.CharField(max_length=300)
    First_Name = models.CharField(max_length=30)
    Middle_Name = models.CharField(blank=True, null=True, max_length=100)
    Last_Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Address_Proof_img_front = models.ImageField(null=True, blank=True, upload_to=APK_Education)
    Address_Proof_img_Back = models.ImageField(null=True, blank=True,upload_to=APK_Education)
    Pan_Card = models.ImageField(null=True, blank=True, upload_to=APK_Education)
    Photo = models.ImageField(null=True, blank=True, upload_to=APK_Education)
    date = models.DateTimeField(auto_now=True)


class Campaign(models.Model):
    sno = models.AutoField(primary_key=True)
    Active = models.BooleanField(default=True)
    Logo = models.ImageField(upload_to='campaign')
    Campaign_Name = models.CharField(max_length=80)
    SMS = models.BooleanField(default=True)
    Mail = models.BooleanField(default=True)
    Mail_body = models.BooleanField(default=True)
    Mail_Subject = models.CharField(max_length=5000, null=True, blank=True)
    Mail_Content = models.CharField(max_length=5000, null=True, blank=True)
    Link = models.CharField(max_length=500, default="")
    Link_Email = models.CharField(max_length=500, default="")
    points = models.IntegerField(null=True)
    Validity = models.DateField()
    Capping = models.IntegerField()
    Description = models.TextField(max_length=5000)
    Terms_and_condition = models.TextField(max_length=5000)
    Does_Exist = models.BooleanField(default=True)
    Does = models.TextField(max_length=5000, null=True, blank=True)
    Dont = models.TextField(max_length=5000, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)


class Form_Campaign(models.Model):
    sno = models.AutoField(primary_key=True)
    User_Email = models.CharField(max_length=400)
    Campaign_Sno = models.CharField(max_length=300)
    Send_on = models.CharField(max_length=500)
    Campaign_Name = models.CharField(max_length=500)
    Conformed = models.BooleanField(default=False)
    Points = models.CharField(max_length=100, null=True, default='-')
    date = models.DateTimeField(auto_now=True)


class Capping(models.Model):
    sno = models.AutoField(primary_key=True)
    Campaign_Sno = models.CharField(max_length=300)
    Campaign_Name = models.CharField(max_length=200)
    capping = models.IntegerField(default=0)
    User_Email = models.CharField(max_length=400)
    Detail = models.CharField(max_length=20000)
    Points = models.IntegerField(default=0)
    Pending_Points = models.IntegerField(default=0)
    Conformed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)


def Form(instance, filename):
    os.path.join('media/Credit_Card', instance.Bank_Name)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dire = '{0}/{1}'.format(instance.Bank_Name, filename)
    return str(dire)


class Credit_Card_Bank(models.Model):
    sno = models.AutoField(primary_key=True)
    Active = models.BooleanField(default=True)
    Bank_Name = models.CharField(max_length=300)
    All_Pin_Code = models.BooleanField(default=False)
    Pin_Code = models.TextField(max_length=350000)
    Document = models.BooleanField(default=False)
    form1 = models.ImageField(null=True, blank=True, upload_to=Form)
    date = models.DateTimeField(auto_now=True)


class Credit_Card_Banking(models.Model):
    sno = models.AutoField(primary_key=True)
    Active = models.BooleanField(default=True)
    Bank_Name = models.CharField(max_length=300)
    fresh_card = models.TextField(max_length=350000)
    Documents = models.TextField(max_length=350000)
    Bank_CardToCard = models.TextField(max_length=350000)
    Payout = models.TextField(max_length=350000)
    date = models.DateTimeField(auto_now=True)

    def fresh_Card(self):
        return self.fresh_card.split(';')

    def documents(self):
        return self.Documents.split(';')

    def Bank_cardToCard(self):
        return self.Bank_CardToCard.split(';')

    def payout(self):
        return self.Payout.split(';')


def credit_cards(instance, filename):
    os.path.join('media/Credit_Card', instance.Customer_Email)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dire = '{0}/{1}'.format(instance.Email, filename)
    return str(dire)


class Credit_Card(models.Model):
    sno = models.AutoField(primary_key=True)
    Status = models.CharField(max_length=400, default='Under Process')
    Action = models.CharField(max_length=400, default='-')
    Merchant_mail = models.CharField(max_length=300)
    Bank_Name = models.CharField(max_length=300)
    Pin_Code = models.CharField(max_length=200)
    Customer_Name = models.CharField(max_length=100)
    Contact = models.CharField(max_length=50)
    ALT_Number = models.CharField(max_length=150)
    Form_Application_Number = models.CharField(max_length=400)
    AGENT_Name = models.CharField(max_length=400)
    Customer_Email = models.CharField(max_length=400)
    Bank_Surrogate = models.CharField(max_length=400)
    Customer_Limit_Salary = models.CharField(max_length=400)
    Pan_Card = models.CharField(max_length=400)
    Points = models.IntegerField(default=0)
    Card_Copy = models.ImageField(null=True, blank=True, upload_to=credit_cards)
    Salary_Slip = models.ImageField(null=True, blank=True, upload_to=credit_cards)
    KYC = models.ImageField(null=True, blank=True, upload_to=credit_cards)
    Photo = models.ImageField(null=True, blank=True, upload_to=credit_cards)
    Official_ID_Card = models.ImageField(null=True, blank=True, upload_to=credit_cards)
    Card_Status = models.CharField(max_length=100, null=True, default='In Process')
    Commission = models.CharField(max_length=100, null=True, default='-')
    date = models.DateTimeField(auto_now=True)
