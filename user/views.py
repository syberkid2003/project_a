from django.shortcuts import render  , redirect ,HttpResponse
from user.models import *
from college.models import *
from university.models import *
from test.models import *
from employee.models import *
from .models import *
from datetime import datetime ,timedelta
import razorpay
import pytz
from django.core.mail import send_mail
from django.conf import  settings
import pyautogui as keyboard
import cv2
from .camara import *
from django.http.response import StreamingHttpResponse


def home(req):
    response = render(req,"user_index.html" , locals())
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    print(name,val_id)
    user = Student.objects.get(id=val_id)
    return render(req,"user_index.html" , locals())

def test(req ):
    val_id = req.COOKIES['id']
    user = Student.objects.get(id=val_id)
    time_now = datetime.now()
    time = datetime.now()
    timezone = pytz.timezone('Asia/Kolkata')
    time =time.astimezone(timezone)
    name  = req.COOKIES['name']
    print(name,val_id)
    if req.method == "POST" :
        sub  = req.POST.get('SUB')
        response = redirect("test_pay")
         
        if sub == "PY":
            response.set_cookie('exam', "PY"  )
            check = Python.objects.filter(user_id = user.hall_no)
            # n = len(check)
            # if check:

            #     for i in check:
                    
            #         if i.pay_time == i.time:
            #             response.set_cookie('exam_id',i.id  )
            #             print(i.id , "old acess")
            #             if i.payment != "False":
            #                 return render(req , "test_pay_info.html",{"trans_id":i.payment})

                        
            #         if (i.test_due) < time:
            #             # data = Python(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now , pay_time =time_now , test_time =time_now , test_due =time_now) 
            #             # data.save()
            #             # user = Student.objects.get(id=val_id)
            #             # 
            #             # user.save()
            #             # response.set_cookie('exam_id',data.id  )
            #             # print(data.id , "new creation")
            #             # break
            #             return render(req , "test_pay_info.html",{"trans_id":"sesion expired!"})
                      
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
                    
                    
            else:
                
                data = Python(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now , pay_time =time_now , test_time =time_now , test_due =time_now) 
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation")

        if sub == "JAVA":
            response.set_cookie('exam', "JAVA"  )
            check = Java.objects.filter(user_id = user.hall_no)
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
            else:
                
                data = Java(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now , pay_time =time_now , test_time =time_now, test_due =time_now) 
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation")
                          
        if sub == "C":
            response.set_cookie('exam', "C"  ) 
            check = Clang.objects.filter(user_id = user.hall_no)
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
            else:
                
                data = Clang(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now, pay_time =time_now , test_time =time_now , test_due =time_now) 
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation")

        if sub == "CPP":
            response.set_cookie('exam', "CPP"  ) 
            check = CPPlang.objects.filter(user_id = user.hall_no)
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
            else:
                
                data = CPPlang(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now, pay_time =time_now , test_time =time_now , test_due =time_now) 
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation")

        if sub == "DBMS":
            response.set_cookie('exam', "DBMS"  )
            check = DBMS.objects.filter(user_id = user.hall_no)
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
            else:
                data = DBMS(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now, pay_time =time_now , test_time =time_now , test_due =time_now) 
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation")  

        if sub == "PHP":
            response.set_cookie('exam', "PHP"  ) 
            check = PHP.objects.filter(user_id = user.hall_no)
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
            else:
                data = PHP(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now, pay_time =time_now , test_time =time_now , test_due =time_now) 
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation") 

        if sub == "HTML":
            response.set_cookie('exam', "HTML"  ) 
            check = HTML.objects.filter(user_id = user.hall_no)
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
            else:
                data = HTML(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now, pay_time =time_now , test_time =time_now , test_due =time_now)  
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation")

        if sub == "JS":
            response.set_cookie('exam', "JS"  )
            check = JavaScript.objects.filter(user_id = user.hall_no)
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
            else:
                data = JavaScript(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now, pay_time =time_now , test_time =time_now , test_due =time_now) 
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation")   

        if sub == "R":
            response.set_cookie('exam', "R"  ) 
            check = Rlang.objects.filter(user_id = user.hall_no)
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
            else:
                data = Rlang(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now, pay_time =time_now , test_time =time_now , test_due =time_now) 
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation") 

        if sub == "CH":
            response.set_cookie('exam', "CH"  )
            check = Chash.objects.filter(user_id = user.hall_no)
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
            else:
                data = Chash(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now, pay_time =time_now , test_time =time_now , test_due =time_now) 
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation") 

        if sub == "GO":
            response.set_cookie('exam', "GO"  )
            check = GOlang.objects.filter(user_id = user.hall_no)
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
            else:
                data = GOlang(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now, pay_time =time_now , test_time =time_now , test_due =time_now) 
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation") 

        if sub == "SWIFT":
            response.set_cookie('exam', "SWIFT"  )
            check = SWIFT.objects.filter(user_id = user.hall_no)
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
            else:
                data = SWIFT(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now, pay_time =time_now , test_time =time_now , test_due =time_now) 
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation")  

        if sub == "RUST":
            response.set_cookie('exam', "RUST"  ) 
            check = RUST.objects.filter(user_id = user.hall_no)
            if check:
                for i in check:
                    if i.test_time != i.time:
                        return redirect('test_result')
                    response.set_cookie('exam_id',i.id  )
                    print(i.id , "old acess")
                    if i.payment != "False":
                        return render(req , "test_pay_info.html",{"trans_id":i.payment})
            else:
                data = RUST(name = user.name , user_id = user.hall_no , test = False , payment =False , time=time_now, pay_time =time_now , test_time =time_now , test_due =time_now) 
                data.save()
                user = Student.objects.get(id=val_id)
                
                user.save()
                response.set_cookie('exam_id',data.id  )
                print(data.id , "new creation") 
    
        return response
    python = Python.objects.filter(user_id = user.hall_no)
    chash  = Chash.objects.filter(user_id = user.hall_no)
    clang  = Clang.objects.filter(user_id = user.hall_no)
    dbms   = DBMS.objects.filter(user_id = user.hall_no)
    golang = GOlang.objects.filter(user_id = user.hall_no)
    html   = HTML.objects.filter(user_id = user.hall_no)
    js     = JavaScript.objects.filter(user_id = user.hall_no)
    java   = Java.objects.filter(user_id = user.hall_no)
    php    = PHP.objects.filter(user_id = user.hall_no)
    rlang  = Rlang.objects.filter(user_id = user.hall_no)
    rust   = RUST.objects.filter(user_id = user.hall_no)
    swift  = SWIFT.objects.filter(user_id = user.hall_no)
    cpplang  = SWIFT.objects.filter(user_id = user.hall_no)

    return render(req , "sub_sel_usr.html" , locals())

def test_pay(req):
    name  = req.COOKIES['name']
    client = razorpay.Client(auth = ("rzp_test_iJhFmgV1x8XFkE", "0fwKAbXKBNwsOt1GwJgHM9Cd"))
    payment = client.order.create({'amount': 100000, "currency" : "INR" , "payment_capture": 1 })
    amount = 100000
    return render(req, "pay_for_test.html" ,locals())

def test_pay_done(req , trans_id):
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    user = Student.objects.get(id=val_id)
    time = datetime.now()
    due = time + timedelta(2) 
    sub = req.COOKIES['exam']
    sub_id = req.COOKIES['exam_id']

    if sub == "PY":
        data = Python.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()

    if sub == "JAVA":
        data = Java.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()
        

    if sub == "C":
        data = Clang.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()
        

    if sub == "CPP":
        data = CPPlang.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()
        

    if sub == "CH":
        data = Chash.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()
        

    if sub == "DBMS":
        data = DBMS.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()
        

    if sub == "PHP":
        data = PHP.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()
        

    if sub == "HTML":
        data = HTML.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()
        

    if sub == "JS":
        data = JavaScript.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()
        

    if sub == "R":
        data = Rlang.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()
        

    if sub == "GO":
        data = GOlang.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()
        

    if sub == "SWIFT":
        data = SWIFT.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()
        

    if sub == "RUST":
        data = RUST.objects.get(id=sub_id)
        data.payment = trans_id
        data.pay_time = time
        data.test_due = due
        data.save()
        


    msg = "hello you requested for take a online test  hear is your test link   http://localhost:8000/test/paid/setup/"+ str(sub) +'/'+str(sub_id)
    send_mail( subject="TEST LINK", message=msg, from_email=settings.EMAIL_HOST_USER,recipient_list=[user.email])
    return render (req, "test_pay_info.html" ,locals())

def take_test_now(req, sub , num):
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    user = Student.objects.get(id=val_id)
    time = datetime.now()
    timezone = pytz.timezone('Asia/Kolkata')
    time =time.astimezone(timezone)
    response = render(req,"test_setup.html")
    response.set_cookie('exam_id',num  )
    if sub == "PY":
        data = Python.objects.get(id=num)

        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time :
                response.set_cookie("current_exam" , "PY") 
                response.set_cookie("subject" , "PYTHON") 
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")


        

    if sub == "JAVA":
        data = Java.objects.get(id=num)
        
        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time : 
                response.set_cookie("current_exam" , "JAVA")
                response.set_cookie("subject" , "JAVA")  
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")

        

    if sub == "C":
        data = Clang.objects.get(id=num)
        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time : 
                response.set_cookie("current_exam" , "C") 
                response.set_cookie("subject" , "C Language") 
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")
        

    if sub == "CPP":
        data = CPPlang.objects.get(id=num)
        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time : 
                response.set_cookie("current_exam" , "CPP") 
                response.set_cookie("subject" , "C++ Language") 
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")
        

    if sub == "CH":
        data = Chash.objects.get(id=num)
        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time : 
                response.set_cookie("current_exam" ,"CH")
                response.set_cookie("subject" , "C# Language") 
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")
        

    if sub == "DBMS":
        data = DBMS.objects.get(id=num)
        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time :
                response.set_cookie("current_exam" , "DBMS")
                response.set_cookie("subject" , "DBMS") 
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")
        

    if sub == "PHP":
        data = PHP.objects.get(id=num)
        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time : 
                response.set_cookie("current_exam" , "PHP")
                response.set_cookie("subject" , "PHP") 
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")
        

    if sub == "HTML":
        data = HTML.objects.get(id=num)
        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time : 
                response.set_cookie("current_exam" , "HTML")
                response.set_cookie("subject" , "HTML") 
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")
        

    if sub == "JS":
        data = JavaScript.objects.get(id=num)
        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time : 
                response.set_cookie("current_exam" , "JS") 
                response.set_cookie("subject" , "Java Script")
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")
        

    if sub == "R":
        data = Rlang.objects.get(id=num)
        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time : 
                response.set_cookie("current_exam" , "R")
                response.set_cookie("subject" , "R Language") 
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")
        

    if sub == "GO":
        data = GOlang.objects.get(id=num)
        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time : 
                response.set_cookie("current_exam" , "GO") 
                response.set_cookie("subject" , "GO Language") 
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")
        

    if sub == "SWIFT":
        data = SWIFT.objects.get(id=num)
        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time : 
                response.set_cookie("current_exam" , "SWIFT")
                response.set_cookie("subject" , "SWIFT Language")  
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")
        

    if sub == "RUST":
        data = RUST.objects.get(id=num)
        if user.hall_no == data.user_id  and data.payment !="False":
            if (data.test_due) >= time : 
                response.set_cookie("current_exam" , "RUST")
                response.set_cookie("subject" , "RUST Language") 
                return response
            else:
                return HttpResponse("YOUR TEST LINK IS EXPIRED  !")
        elif user.hall_no != data.user_id  :
            return HttpResponse("your trying to take others test! this can lead to your De-Bar")
        elif data.payment == "False" :
            return HttpResponse("YOU HAVEN'T PAID FOR TEST!")
        
        else:
            return HttpResponse("some thing went wrong!")
        
    
    return redirect("user_home")

def test_ongoing(req):
    response = render(req,"user_test_ongoing.html" , locals())
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    sub = req.COOKIES['current_exam']
    subject = req.COOKIES['subject']
    exam_id = req.COOKIES['exam_id']
    user = Student.objects.get(id=val_id)
    keyboard.press('f11')
    if req.method == "POST" :
        timezone = pytz.timezone('Asia/Kolkata')
        index = req.session.get("index" , [])
        time = timezone.localize(datetime.now())
        test = Test(time = time ,student = name , marks = 0 , hall_ticket = user.hall_no , college_code = user.clg_code , uni = user.university,clg=user.college)
        test.save()
        for i in index:
            question = Question.objects.get(id=i)
            try:
                if req.POST.get(question.problem) == question.ans:
                    test.marks += 1
                    test.save()
                else:
                    print("no" , question.ans)
                result = Result(name = name , question = question.problem ,answer = question.ans ,submit =req.POST.get(question.problem) ,test_id = test.id  )
                result.save()
            except :
                result = Result(name = name , question = question.problem ,answer = question.ans ,submit ="Empty" ,test_id = test.id  )
                result.save()

        
        # time =time.astimezone(timezone)
        if sub == "PY":
            subject = "PYTHON"
            exam = Python.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()

        if sub == "JAVA":
            subject = "JAVA"
            exam = Java.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()

        if sub == "C":
            subject = "C Language"
            exam = Clang.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()

        if sub == "CPP":
            subject = "C++ Language"
            exam = CPPlang.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()

        if sub == "DBMS":
            subject = "DBMS"
            exam = DBMS.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()

        if sub == "JS":
            subject = "Java Script"
            exam = JavaScript.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()

        if sub == "R":
            subject = "R Language"
            exam = Rlang.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()

        if sub == "CH":
            subject = "C# Language"
            exam = Chash.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()

        if sub == "GO":
            subject = "GO Language"
            exam = GOlang.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()

        if sub == "SWIFT":
            subject = "SWIFT Language"
            exam = SWIFT.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()

        if sub == "RUST":
            subject = "RUST Language"
            exam = RUST.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()

        if sub == "HTML":
            subject = "HTML Language"
            exam = HTML.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()
        
        if sub == "PHP":
            subject = "PHP Language"
            exam = PHP.objects.get(id=exam_id)
            exam.test_time = time
            exam.test = test.id
            exam.save()
        
        # keyboard.press("f11")
        return render(req,"test_done.html")
    
    questions = []   

    
    data = Question.objects.filter(sub = sub)
    index = []
    for i in data:

        if user.clg_code == "None" and i.id not in index:
            index.append(i.id)
        else:
            if i.uni == user.university and i.id not in index and i.clg == "False":
                index.append(i.id)
            elif i.clg == user.clg_code and i.id not in index:
                index.append(i.id)
            else:
                pass
        # ser_index = json.dumps(index)

    req.session['index'] = index

    
    index = req.session.get("index" , [])
    for i in index:
        questions.append(Question.objects.get(id=i))
    
    return render(req,"user_test_ongoing.html" , locals())

def test_result(req):
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    user = Student.objects.get(id=val_id)
    python = Python.objects.filter(user_id = user.hall_no)
    time = datetime.now()
    for i in python:
        time = i.time
    python = python.exclude(test_time= time)

    chash  = Chash.objects.filter(user_id = user.hall_no)
    for i in chash:
        time = i.time
    chash = chash.exclude(test_time=time)

    clang  = Clang.objects.filter(user_id = user.hall_no)
    for i in chash:
        time = i.time
    clang = clang.exclude(test_time=time)

    dbms   = DBMS.objects.filter(user_id = user.hall_no)
    for i in dbms:
        time = i.time
    dbms   = dbms.exclude(test_time= time) 

    golang = GOlang.objects.filter(user_id = user.hall_no)
    for i in golang:
        time = i.time
    golang = golang.exclude(test_time= time)

    html   = HTML.objects.filter(user_id = user.hall_no)
    for i in html:
        time = i.time
    html   = html.exclude(test_time= time)

    js     = JavaScript.objects.filter(user_id = user.hall_no)
    for i in js:
        time = i.time
    js     = js.exclude(test_time= time) 

    java   = Java.objects.filter(user_id = user.hall_no)
    for i in java:
        time = i.time
    java   = java.exclude(test_time= time)

    php    = PHP.objects.filter(user_id = user.hall_no)
    for i in chash:
        time = i.time
    php    = php.exclude(test_time= time)

    rlang  = Rlang.objects.filter(user_id = user.hall_no)
    for i in rlang:
        time = i.time
    rlang  = rlang.exclude(test_time= time)

    rust   = RUST.objects.filter(user_id = user.hall_no)
    for i in rust:
        time = i.time
    rust   = rust.exclude(test_time= time)

    swift  = SWIFT.objects.filter(user_id = user.hall_no)
    for i in swift:
        time = i.time
    swift  = swift.exclude(test_time= time)

    cpplang  = CPPlang.objects.filter(user_id = user.hall_no)
    for i in cpplang:
        time = i.time
    cpplang  = cpplang.exclude(test_time= time)  

    return render(req,"test_result.html" , locals())

def deep_result(req,sub,num):
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    user = Student.objects.get(id=val_id)
    if sub=='PY':
        python = Python.objects.get(id=num)
        _id = python.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)

    if sub=='JAVA':
        java = Java.objects.get(id=num)
        _id = java.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)
    
    if sub=='JS':
        js = JavaScript.objects.get(id=num)
        _id = js.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)

    if sub=='CH':
        chash = Chash.objects.get(id=num)
        _id = chash.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)

    if sub=='C':
        clang = Clang.objects.get(id=num)
        _id = clang.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)
    
    if sub=='CPP':
        cpp = CPPlang.objects.get(id=num)
        _id = js.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)
    
    if sub=='DBMS':
        dbms = DBMS.objects.get(id=num)
        _id = dbms.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)

    if sub=='GO':
        go = GOlang.objects.get(id=num)
        _id = go.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)
    
    if sub=='HTML':
        html = HTML.objects.get(id=num)
        _id = html.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)

    if sub=='PHP':
        php = PHP.objects.get(id=num)
        _id = php.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)
    
    if sub=='R':
        rlang = DBMS.objects.get(id=num)
        _id = dbms.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)

    if sub=='RUST':
        rust = RUST.objects.get(id=num)
        _id = rust.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)
    
    if sub=='SWIFT':
        swift = SWIFT.objects.get(id=num)
        _id = swift.test
        data = Test.objects.get(id=_id)
        test = Result.objects.filter(test_id=data.id)

    return render(req,"deep_results.html" , locals())

def user_profile(req):
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    student = Student.objects.get(id=val_id)
    
    return render(req,"user_profile.html" , locals())

def update_user_profile (req):
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    student = Student.objects.get(id=val_id)
    if req.method == "POST" :
        name = req.POST.get("name")
        hall = req.POST.get("hall")
        phno = req.POST.get("phno")
        clg = req.POST.get("clg")
        clg_code = req.POST.get("clg_code")
        uni = req.POST.get("uni")
        user  = req.POST.get("user")
        if req.FILES.get("pic") == None:
             pic = student.profile
        else:
             pic = req.FILES.get("pic")
        student.name = name
        student.contact = phno
        student.hall_no = hall
        student.college =  clg
        student.clg_code = clg_code
        student.university = uni
        student.user_name = user
        student.profile = pic
        student.save()
    return render(req,"update_stu_pro.html" , locals())

def user_support(req):
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    user = Student.objects.get(id = val_id)
    if req.method == "POST":
        title = req.POST.get('name')
        description = req.POST.get("description")
        data = CustomerSupport(name = name , title = title , _from = "Student" , emp_id = user.hall_no , description = description ,solution = False )
        data.save()
        msg = "we under stand your problem our member will respond as soon as possible!"

    
    return render(req,"user_support.html" , locals())

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed_alert(req ):
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 140)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    sub = req.COOKIES['current_exam']
    id = req.COOKIES['exam_id']
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    user = Student.objects.get(id=val_id)
    face_tracker = FaceTracker(name,user.hall_no,sub,id)
    return StreamingHttpResponse(face_tracker.gen(), content_type='multipart/x-mixed-replace; boundary=frame')

def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')




#comment

