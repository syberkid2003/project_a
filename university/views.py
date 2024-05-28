from django.shortcuts import render ,redirect
from .models import *
from user.models import *
from college.models import *
from django.db.models import Q
from test.models import *
from employee.models import *
# Create your views here.
def uni_home(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    uni = University.objects.get(id =val_id) 
    clg_data = College.objects.filter(university = uni.uni)
    stu_data = Student.objects.filter(university = uni.uni)
    return render(req,"university_index.html" , locals())

def colleges(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    check = University.objects.get(id =val_id)
    data = College.objects.filter(university = check.uni)
    return render(req , "colleges.html" , locals())

def uni_students(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    check = University.objects.get(id =val_id)
    data = Student.objects.filter(university = check.uni)
    return render(req , "uni_stu.html" , locals())

def uni_search(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    query = req.GET["search"]
    print(query)
    if query != None:
            child = []
            colleges = College.objects.filter(clg_code = query)

            check = University.objects.get(id =val_id)
            text = "College Not found!"
            for i in colleges:
                if i.university ==  check.uni:
                     text = None
                     child.append(i)
            students = Student.objects.filter(clg_code = child[0].clg_code)
            return render (req , "university_search.html" , locals())
 
    
    # return render(req , "clg_profile_uni.html" , locals())

def uni_test_add(req):
     name = req.COOKIES['name']
     val_id = req.COOKIES['id']
     text = None
     check = University.objects.get(id =val_id)
     if req.method == "POST" :
        question = req.POST.get('name')
        a = req.POST.get('a')
        b = req.POST.get('b')
        c = req.POST.get('c')
        d= req.POST.get('d')
        ans = req.POST.get('ans')
        sub = req.POST.get('sub')
        data = Question(problem =question , a =a , b= b ,c= c , d =d ,ans= ans , sub = sub , uni= check.uni  , clg = False )
        data.save()
        text = "Question is added to  Data Base!"
        return render(req , "uni_test_add.html" , locals())
     return render(req , "uni_test_add.html" , locals())

def uni_search_stu(req):
    name = req.COOKIES['name']
    query = req.GET["search"]
    if query != None:
            child = []
            val_id = req.COOKIES['id']
            data = Student.objects.filter(hall_no = query)
            check = University.objects.get(id =val_id)
            text = "Student Not found!"
            for i in data:
                if i.university ==  check.uni:
                     text = None
                     child.append(i)
    return render(req , "uni_search_stu.html",locals())

def uni_search_clg(req):
    name = req.COOKIES['name']
    query = req.GET["search"]
    print(query)
    if query != None:
            child = []
            val_id = req.COOKIES['id']
            data = College.objects.filter(clg_code = query)
            check = University.objects.get(id =val_id)
            text = "College Not found!"
            for i in data:
                if i.university ==  check.uni:
                     text = None
                     child.append(i)
            return render(req , "uni_search_clg.html" , locals())

def student_profile_uni(req , num):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    university  = University.objects.get(id =val_id)
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
     
    return render(req ,"student_profile_uni.html" , locals())

def uni_deep_result(req , sub , num):
     name = req.COOKIES['name']
     val_id = req.COOKIES['id']
     university = University.objects.get(id =val_id)
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
     
     return render(req,"uni_stu_results.html" , locals())

def clg_profile_uni (req ,num):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    university  = University.objects.get(id =val_id)  
    college = College.objects.get(id = num) 
    data = Student.objects.filter(clg_code = college.clg_code)
    return render(req , "clg_profile_uni.html" , locals())

def uni_profile(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    uni = University.objects.get(id =val_id) 
    return render(req , "uni_profile.html" ,locals())

def uni_support(req):
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    user = University.objects.get(id = val_id)
    if req.method == "POST":
        title = req.POST.get('name')
        description = req.POST.get("description")
        data = CustomerSupport(name = name , title = title , by_from = "University" , emp_id = user.uni , description = description ,solution = False )
        data.save()
        msg = "we under stand your problem our member will respond as soon as possible!"

    
    return render(req,"uni_support.html" , locals())




def chat_uni(req):
    name = req.COOKIES.get('name')
    val_id = req.COOKIES.get('id')
    user = University.objects.get(id=val_id)
    chat = messsanger.objects.filter(sender_id = user.id , sender_type="university")

    return render(req,"uni_chat.html" ,locals())


def send_msg_uni(req):
    name = req.COOKIES.get('name')
    val_id = req.COOKIES.get('id')
    msg  = req.GET['msg']
    new = messsanger(name =name , msg = msg , sender_id = val_id , sender_type = "university" , created = "user")
    new.save()
    return redirect('uni_chat')



#comment