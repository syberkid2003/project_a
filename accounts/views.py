from django.shortcuts import render , redirect
import random
from user.models import *
from college.models import *
from super.models import *
from school.models import *
from university.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import  settings
from django.contrib.auth.models import User
# from django.core.signing import Signer

# Create your views here.

def signup_as(req):
    if req.method == "POST" :
        kind = req.POST.get('kind')
        response = redirect("signup")
        if kind == "College":
            response.set_cookie('Username', "College Name" ) 
            response.set_cookie('location', "City" ) 
            response.set_cookie('code', "Postal Code" ) 
            response.set_cookie('userid', "PRINCIPAL" ) 
            
        if kind == "Student":
            response.set_cookie('Username', "Full Name" ) 
            response.set_cookie('location', "College Name" ) 
            response.set_cookie('code', "Hall Ticket Number" ) 
            response.set_cookie('userid', "User ID" ) 
        
        response.set_cookie('kind', kind ) 
        return response
    
    return render(req , "signup_as.html")

@csrf_exempt
def signup(req):
    kind  = req.COOKIES['kind']
    Username  = req.COOKIES['Username']
    location  = req.COOKIES['location']
    coder  = req.COOKIES['code']
    userid  = req.COOKIES['userid']
    if req.method == "POST" :
        name = req.POST.get('name')
        user = req.POST.get("user")
        mail = req.POST.get("mail")
        pswd = req.POST.get("pswd1")
        pswd2 = req.POST.get("pswd2")
        code = req.POST.get("code")
        clg = req.POST.get("clg")
        clg_code = req.POST.get("clg_code")
        uni = req.POST.get('uni')
        pic = req.POST.get('image')
        terms = req.POST.get("terms")
        #superuser check
        superusers = User.objects.filter(is_superuser=True)
        for i in superusers:
            if  mail == i.email:
                error =  "this mail   already have account, please login !"
                return render (req , "signup.html" , locals() )
        
        #University  check 
        data = University.objects.all()
        for i in data:
            if  mail == i.email or user == i.contact or pic == i.name :
                if pswd == pswd2:
                    if mail == i.email:  
                            error = "this mail already have account, please login !"
                            return render (req , "signup.html" , locals())
                    elif pic == i.name and kind != "College":
                        error= "this USER ID  already  Exitst !"
                        return render (req , "signup.html" , locals())
                    else:
                        error ="this contact  already have account, please login !"
                        return render (req , "signup.html" , locals() )
                else:
                    error = "re-enterd password didn't sink with password !"
                    return render (req , "signup.html" , locals()  )

        #college  check 
        data = College.objects.all()
        for i in data:
            if  mail == i.email or user == i.contact or pic == i.name :
                    if pswd == pswd2:
                        if mail == i.email:  
                                error = "this mail already have account, please login !"
                                return render (req , "signup.html" , locals())
                        elif pic == i.name and kind != "College":
                            error= "this USER ID  already  Exitst !"
                            return render (req , "signup.html" , locals())
                        else:
                            error ="this contact  already have account, please login !"
                            return render (req , "signup.html" , locals() )
                    else:
                        error = "re-enterd password didn't sink with password !"
                        return render (req , "signup.html" , locals()  )

        #scholl  check 
        data = School.objects.all()
        for i in data:
            if  mail == i.email or user == i.contact or pic == i.name :
                    if pswd == pswd2:
                        if mail == i.email:  
                                error = "this mail already have account, please login !"
                                return render (req , "signup.html" , locals())
                        elif pic == i.name and kind != "College":
                            error= "this USER ID  already  Exitst !"
                            return render (req , "signup.html" , locals())
                        else:
                            error ="this contact  already have account, please login !"
                            return render (req , "signup.html" , locals() )
                    else:
                        error = "re-enterd password didn't sink with password !"
                        return render (req , "signup.html" , locals()  )
        #student  check 
        data = Student.objects.all()
        for i in data:
            if  mail == i.email or user == i.contact or pic == i.name :
                    if pswd == pswd2:
                        if mail == i.email:  
                                error = "this mail already have account, please login !"
                                return render (req , "signup.html" , locals())
                        elif pic == i.user_name and kind != "College":
                            error= "this USER ID  already  Exitst !"
                            return render (req , "signup.html" , locals())
                        else:
                            error ="this contact  already have account, please login !"
                            return render (req , "signup.html" , locals() )
                    else:
                        error = "re-enterd password didn't sink with password !"
                        return render (req , "signup.html" , locals()  )
        otp = ''
        while True:
            x = random.randint(0,9)
            otp += str(x) 
            if len(otp) == 6:
                break 
        response = redirect("mail")
        response.set_cookie('name', name )  
        response.set_cookie('contact', user)
        response.set_cookie('email', mail)
        response.set_cookie('pswd', pswd)
        response.set_cookie('otp', otp)
        response.set_cookie('code', code)
        response.set_cookie('clg', clg)
        response.set_cookie('clg_code', clg_code)
        response.set_cookie('uni', uni)
        response.set_cookie('user', pic)
        response.set_cookie('terms', terms)
        
        
        msg = "hello you requested for signup  hear is your one time password(otp)  for creating account "+ otp
        send_mail( subject="ACCOUNT VRIFICATION", message=msg, from_email=settings.EMAIL_HOST_USER,recipient_list=[mail]) 
        return response
    
    return render(req ,"signup.html" , locals())

def mail_verify (req):
    otp2 = req.COOKIES['otp']
    print(otp2)
    
    if req.method == "POST" :
        
        otp1 = req.POST.get('otp')
        name = req.COOKIES['name']
        user = req.COOKIES['contact']
        mail = req.COOKIES['email']
        pswd = req.COOKIES['pswd']
        kind = req.COOKIES['kind']
        code = req.COOKIES['code']
        clg = req.COOKIES['clg']
        clg_code = req.COOKIES['clg_code']
        uni = req.COOKIES['uni']
        user_id = req.COOKIES['user']
        terms = req.COOKIES['terms']
        

        if otp1 == otp2:
            
            if kind == "Student":
                user = Student.objects.create(name = name , contact= user , email = mail , password = pswd ,college = clg , clg_code = clg_code , hall_no = code , university = uni , terms= terms , user_name = user_id  , profile = 'profile/user.png')
                # user.save()
            if kind == "College":
                college = College(name = name , contact= user , email = mail , password = pswd  , city= clg , clg_code = clg_code , postal = code , university = uni,terms= terms , principal = user_id  , profile = 'profile/user.png')
                college.save()
            if kind == "School":
                school = School(name = name , contact= user , email = mail , password = pswd )
                school.save()
            return redirect("login")

        return render(req , "mailVerify.html" , {"error":'you enterd wrong otp' })
    return render(req , "mailVerify.html")

@csrf_exempt
def login(req):
    
    if req.method == "GET":
        return render(req, "login.html")
    
    if req.method == "POST":
        mail = req.POST.get("email")
        password = req.POST.get("password")      
        #superuser login
        superusers = User.objects.filter(is_superuser=True)
        for i in superusers:
            if  mail == i.email:
                if password == i.username:
                    otp = ''
                    while True:
                        x = random.randint(0,9)
                        otp += str(x) 
                        if len(otp) == 4:
                            break 
                    print(otp)
                    response = redirect("otp")
                    response.set_cookie('name', i.username)  
                    response.set_cookie('id', i.id)
                    response.set_cookie('otp', otp)
                    response.set_cookie('admin', "yes")

                    msg = "hello you requested for login  hear is your one time password(otp)  for login to your  account "+ otp
                    send_mail( subject="LOGIN VRIFICATION", message=msg, from_email=settings.EMAIL_HOST_USER,recipient_list=[mail]) 


                    return response
                
                else:
                    return render (req , "login.html" , {"error" : "this is a wrong password!" })
                
        employee = Employ.objects.all()
        for i in employee:
            if  mail == i.email:
                if password == i.password:
                    otp = ''
                    while True:
                        x = random.randint(0,9)
                        otp += str(x) 
                        if len(otp) == 4:
                            break 
                    print(otp)
                    response = redirect("otp")
                    response.set_cookie('name', i.name)  
                    response.set_cookie('id', i.id)
                    response.set_cookie('otp', otp)
                    response.set_cookie('admin', "employee")

                    msg = "hello you requested for login  hear is your one time password(otp)  for login to your  account "+ otp
                    send_mail( subject="LOGIN VRIFICATION", message=msg, from_email=settings.EMAIL_HOST_USER,recipient_list=[mail]) 


                    return response
                
                else:
                    return render (req , "login.html" , {"error" : "this is a wrong password!" })


        #university login
        university = University.objects.all()
        for i in university:
            if  mail == i.email:
                if password == i.password:
                    otp = ''
                    while True:
                        x = random.randint(0,9)
                        otp += str(x) 
                        if len(otp) == 4:
                            break 
                    print(otp)
                    response = redirect("otp")
                    response.set_cookie('name', i.name)  
                    response.set_cookie('id', i.id)
                    response.set_cookie('otp', otp)
                    response.set_cookie('admin', "university")

                    msg = "hello you requested for login  hear is your one time password(otp)  for login to your  account "+ otp
                    send_mail( subject="LOGIN VRIFICATION", message=msg, from_email=settings.EMAIL_HOST_USER,recipient_list=[mail]) 


                    return response
                
                else:
                    return render (req , "login.html" , {"error" : "this is a wrong password!" })


        #college login
        data = College.objects.all()
        for i in data:
            if  mail == i.email or mail == i.contact :
                if password == i.password:
                    otp = ''
                    while True:
                        x = random.randint(0,9)
                        otp += str(x) 
                        if len(otp) == 4:
                            break 
                    response = redirect("otp")
                    print(otp)
                    response.set_cookie('name', i.name)  
                    response.set_cookie('id', i.id)
                    response.set_cookie('otp', otp)
                    response.set_cookie('admin', "College")

                    msg = "hello you requested for login  hear is your one time password(otp)  for login to your  account "+ otp
                    send_mail( subject="LOGIN VRIFICATION", message=msg, from_email=settings.EMAIL_HOST_USER,recipient_list=[mail]) 


                    return response
                
                else:
                    return render (req , "login.html" , {"error" : "this is a wrong password!" })
        
        #school login
        data = School.objects.all()
        for i in data:
            if  mail == i.email or mail == i.contact :
                if password == i.password:
                    otp = ''
                    while True:
                        x = random.randint(0,9)
                        otp += str(x) 
                        if len(otp) == 4:
                            break 
                    response = redirect("otp")
                    response.set_cookie('name', i.name)  
                    response.set_cookie('id', i.id)
                    response.set_cookie('otp', otp)
                    response.set_cookie('admin', "School")

                    msg = "hello you requested for login  hear is your one time password(otp)  for login to your  account "+ otp
                    send_mail( subject="LOGIN VRIFICATION", message=msg, from_email=settings.EMAIL_HOST_USER,recipient_list=[mail]) 


                    return response
                
                else:
                    return render (req , "login.html" , {"error" : "this is a wrong password!" })
        

        #normal user(student)
        data = Student.objects.all()
        for i in data:
            if  mail == i.email or mail == i.contact :
                if password == i.password:
                    otp = ''
                    while True:
                        x = random.randint(0,9)
                        otp += str(x) 
                        if len(otp) == 4:
                            break 
                    print(otp)
                    response = redirect("otp")
                    response.set_cookie('name', i.name)  
                    response.set_cookie('id', i.id)
                    response.set_cookie('otp', otp)
                    response.set_cookie('admin', "Student")

                    msg = "hello you requested for login  hear is your one time password(otp)  for login to your  account "+ otp
                    send_mail( subject="LOGIN VRIFICATION", message=msg, from_email=settings.EMAIL_HOST_USER,recipient_list=[mail]) 


                    return response
                
                else:
                    return render (req , "login.html" , {"error" : "this is a wrong password!" })
                

        return render (req , "login.html" , {"error" : "this user is not regesterd!" })
    return render(req ,"login.html")

def login_verify (req):
    
    if req.method == "POST" :
        otp1 = req.POST.get('otp')
        otp2 = req.COOKIES['otp']
        check = req.COOKIES['admin']
        print(otp1 , otp2)
        if otp1 == otp2:
            if check == "yes":
                return redirect("super_admin_home")
            if check == "College":
                return redirect ("college_home")
            if check == "Student":
                return redirect("user_home")
            if check == "university":
                return redirect("uni_home")
            if check == "employee":
                return redirect("emp_home")


        return render(req , "login_verify.html" , {"error":'you enterd wrong otp' })
    return render(req , "login_verify.html")

def logout(req):
    return render(req , "logout.html")


def forgot(req):
    if req.method == "POST":
        mail = req.POST.get("email")
        print(mail)
        data = Student.objects.all()
        for i in data:
            if  mail == i.email :
                url = "http://localhost:8000/settings/login-unable/forgot-passkey/reset-password/"+ str(i.id)
                msg = "hello you requested for password reset  hear is your link  for password changing "+url
                send_mail( subject="PASSWORD RESET", message=msg, from_email=settings.EMAIL_HOST_USER,recipient_list=[mail])            
                return render (req , "passmailsend.html" , {'head':'Mail Send!','msg':"we send a mail to your given mail id verify it and update your password ."})

        return render (req , "forgotPass.html" , {"error" : "this email is not regesterd!" })
        
    return render(req ,"forgotPass.html" , {"msg":'Enter your email and instructions will be sent to you!'})

def reset(req , key):
    data = Student.objects.get(id= key)
    if req.method == "POST" :
        pswd = req.POST.get("pswd1")
        pswd2 = req.POST.get("pswd2")
        if pswd == pswd2: 
            data.password = pswd
            data.save()
            return render (req , "passmailsend.html" , {'head':'password updated!','msg':"your password is updated ,go back to login!."})
        return render(req , "reset.html" ,  {"error" : "password and re-enterd password is not matched!" } )

    return render(req , "reset.html" )

def updatedpasskey(req):
    return render(req, "passlogin.html")

def lock_screen(req):
    check = req.COOKIES['admin']
    if req.method == "POST" :
        name = req.COOKIES['name']
        val_id = req.COOKIES['id']
        print(name , val_id , "lock screen")
        print(type(check))
        passkey =req.POST.get("check")

        if check == "yes":
            user =  User.objects.get(id=val_id)
            if user.password == passkey :
                return redirect("super_admin_home")
        if check == "College":
            user =  College.objects.get(id=val_id)
            if user.password == passkey :
                return redirect("college_home")
            
        if check == "Student":
            user =  Student.objects.get(id=val_id)
            if user.password == passkey :
                return redirect("user_home")
            
        if check == "university":
            user =  University.objects.get(id=val_id)
            if user.password == passkey :
                return redirect("uni_home")
        print( name , val_id , check)
        return render(req , "lockscreen.html" , {"error":"wrong password" , 'user_name':name})
    return render(req , "lockscreen.html")

def chanage_passkey(req):
    val_id = req.COOKIES['id']
    check = req.COOKIES['admin']
    name = req.COOKIES['name']
    if check == "yes":
        user =  User.objects.get(id=val_id)
    if check == "College":
        user =  College.objects.get(id=val_id)
    if check == "Student":
        user =  Student.objects.get(id=val_id)
    if check == "university":
        user =  University.objects.get(id=val_id)
    if req.method == "POST":
        old = req.POST.get("old")
        new = req.POST.get("new")
        new2 = req.POST.get("new2")
        
        if user.password == old:
            if new == new2 and new != "":
                user.password = new
                user.save()
                return render(req , "changepass.html" , {'suc':'Your Password is Updated!'})
            return render(req , "changepass.html" , {'error':'The re-enterd password is not matched!'})
        return render(req , "changepass.html",{'error':'Enter the password correctly!'})
    # print(user.name , user.password , user.email)
    if check == "yes":
        return render(req , "changepass.html" , locals())
    if check == "College":
        return render(req , "clg_change_passkey.html" , locals())
    if check == "Student":
        return render(req , "changepass.html" , locals())
    if check == "university":
        return render(req , "changepass_uni.html" , locals())

    
