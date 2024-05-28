from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from college.models import *
from user.models import *
from test.models import *
from django.http.response import StreamingHttpResponse
from university.models import *
import time
from django.db.models import Q
from .models import *
# Create your views here.

def admin_home(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    return render(req,"super_admin_index.html")

def admin_uni(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    return render(req,"super_admin_uni.html")

def admin_clg(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    data = College.objects.all()
    x = len(data)
    return render(req,"super_admin_clg.html" ,locals())

def admin_stu(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    data = Student.objects.all()
    x = len(data)
    return render(req,"super_admin_stu.html" , locals())

def admin_clg_search(req): 
    query = req.GET["search"]
    colleges = College.objects.filter(clg_code = query)
    return render(req , "admin_clg_search.html", locals())

def admin_stu_search(req): 
    query = req.GET["search"]
    students = Student.objects.filter(hall_no = query)
    return render(req , "admin_std_search.html", locals())

def student_profile_super(req, num):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    student = Student.objects.get(id=num)
    python = Python.objects.filter(user_id = student.hall_no).exclude(test=0)
    chash  = Chash.objects.filter(user_id = student.hall_no).exclude(test=0)
    clang  = Clang.objects.filter(user_id = student.hall_no).exclude(test=0)
    dbms   = DBMS.objects.filter(user_id = student.hall_no).exclude(test=0)
    golang = GOlang.objects.filter(user_id = student.hall_no).exclude(test=0)
    html   = HTML.objects.filter(user_id = student.hall_no).exclude(test=0)
    js     = JavaScript.objects.filter(user_id = student.hall_no).exclude(test=0)
    java   = Java.objects.filter(user_id = student.hall_no).exclude(test=0)
    php    = PHP.objects.filter(user_id = student.hall_no).exclude(test=0)
    rlang  = Rlang.objects.filter(user_id = student.hall_no).exclude(test=0)
    rust   = RUST.objects.filter(user_id = student.hall_no).exclude(test=0)
    swift  = SWIFT.objects.filter(user_id = student.hall_no).exclude(test=0) 
    cpplang  = SWIFT.objects.filter(user_id = student.hall_no).exclude(test=0)

    python_pay = Python.objects.filter(user_id = student.hall_no)
    chash_pay  = Chash.objects.filter(user_id = student.hall_no)
    clang_pay  = Clang.objects.filter(user_id = student.hall_no)
    dbms_pay   = DBMS.objects.filter(user_id = student.hall_no)
    golang_pay = GOlang.objects.filter(user_id = student.hall_no)
    html_pay   = HTML.objects.filter(user_id = student.hall_no)
    js_pay     = JavaScript.objects.filter(user_id = student.hall_no)
    java_pay   = Java.objects.filter(user_id = student.hall_no)
    php_pay    = PHP.objects.filter(user_id = student.hall_no)
    rlang_pay  = Rlang.objects.filter(user_id = student.hall_no)
    rust_pay   = RUST.objects.filter(user_id = student.hall_no)
    swift_pay  = SWIFT.objects.filter(user_id = student.hall_no)
    cpplang_pay  = SWIFT.objects.filter(user_id = student.hall_no)
    return render(req , "student_profile_super.html", locals())

def super_deep_result(req, sub , num):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
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
     
    return render(req,"super_stu_results.html" , locals())

def clg_profile_super (req ,num): 
    college = College.objects.get(id = num) 
    data = Student.objects.filter(clg_code = college.clg_code)
    return render(req , "clg_profile_super.html" , locals())

def images(req ,sub ,num): 
    print(sub,num)
    videos = Cheat_sheet.objects.filter(test=sub).exclude(~Q(test_id=num))
    for video in videos: 
        with video.pic.open('rb') as f:  # Open the image file in binary mode
            image_bytes = f.read()  # Read the image data as bytes
        yield (b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n\r\n')
        time.sleep(0.3) 

def video_feed_VIDEO(req , sub , num):
    return StreamingHttpResponse(images(req,sub ,num), content_type='multipart/x-mixed-replace; boundary=frame')


def add_emp(req):
    if req.method == "POST" :
        name = req.POST.get('name')
        user = req.POST.get("contact")
        mail = req.POST.get("mail")
        pswd = req.POST.get("pswd1")
        emp_id= req.POST.get("emp_id")
        description = req.POST.get("description")
        role = req.POST.get('uni')
        pic = req.FILES.get('pic')
        terms = req.POST.get("terms")
        data = Employ(name = name, contact = user , emp_id = emp_id , email = mail , password = pswd ,role = role ,description = description ,designation = terms ,profile = pic )
        data.save()
        return render(req ,"add_emp_sup.html", {"msg":"employee"+name+"added to database!"})
    return render(req ,"add_emp_sup.html")