from django.shortcuts import render , redirect
from .models import *
from user.models import *
from university.models import *
from django.db.models import Q
from test.models import *
from employee.models import *

# Create your views here.
def college_home(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    college = College.objects.get(id =val_id)
    data = Student.objects.filter(clg_code = college.clg_code)
    students = []
    test_taken = []
    test_compleat = []
    tests = []


    for i in data:
         students.append(i.hall_no)
    x = len(data)
    subjects = [Python.objects.all(),Java.objects.all(),JavaScript.objects.all(),HTML.objects.all(),PHP.objects.all(),Rlang.objects.all(),RUST.objects.all(),SWIFT.objects.all(),Clang.objects.all(),CPPlang.objects.all(),Chash.objects.all(),GOlang.objects.all(),DBMS.objects.all()] 
    for data in subjects:
         for subject in data:
              for i in students:
                   if i == subject.user_id:
                        test_taken.append(subject)
                        if subject.time != subject.test_time:
                             test_compleat.append(subject)

    
    y = len(test_taken)
    z = len(test_compleat)
                    
    response =render(req,"college_index.html" , locals())
    response.set_cookie('x' , x)
    response.set_cookie('y' , y)
    response.set_cookie('z' , z)
    

                   
    return response

def students(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    college = College.objects.get(id =val_id)
    x = req.COOKIES['x']
    y = req.COOKIES['y']
    z = req.COOKIES['z']
    pending = int(y) - int(z)
    data = Student.objects.filter(clg_code = college.clg_code)
    return render(req , "students.html" , locals())

def college_search(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    query = req.GET["search"]
    college = College.objects.get(id =val_id)
    if query != None:
            child = []
            val_id = req.COOKIES['id']
            student = Student.objects.filter(hall_no = query)
            check = College.objects.get(id =val_id)
            text = "Student Not found!"

            for i in student:
               if i.clg_code ==  check.clg_code:
                  text = None
                  child.append(i)
               python = Python.objects.filter(user_id = i.hall_no).exclude(test=0)
               chash  = Chash.objects.filter(user_id = i.hall_no).exclude(test=0)
               clang  = Clang.objects.filter(user_id = i.hall_no).exclude(test=0)
               dbms   = DBMS.objects.filter(user_id = i.hall_no).exclude(test=0)
               golang = GOlang.objects.filter(user_id = i.hall_no).exclude(test=0)
               html   = HTML.objects.filter(user_id = i.hall_no).exclude(test=0)
               js     = JavaScript.objects.filter(user_id = i.hall_no).exclude(test=0)
               java   = Java.objects.filter(user_id = i.hall_no).exclude(test=0)
               php    = PHP.objects.filter(user_id = i.hall_no).exclude(test=0)
               rlang  = Rlang.objects.filter(user_id = i.hall_no).exclude(test=0)
               rust   = RUST.objects.filter(user_id = i.hall_no).exclude(test=0)
               swift  = SWIFT.objects.filter(user_id = i.hall_no).exclude(test=0) 
               cpplang  = SWIFT.objects.filter(user_id = i.hall_no).exclude(test=0)

               python_pay = Python.objects.filter(user_id = i.hall_no)
               chash_pay  = Chash.objects.filter(user_id = i.hall_no)
               clang_pay  = Clang.objects.filter(user_id = i.hall_no)
               dbms_pay   = DBMS.objects.filter(user_id = i.hall_no)
               golang_pay = GOlang.objects.filter(user_id = i.hall_no)
               html_pay   = HTML.objects.filter(user_id = i.hall_no)
               js_pay     = JavaScript.objects.filter(user_id = i.hall_no)
               java_pay   = Java.objects.filter(user_id = i.hall_no)
               php_pay    = PHP.objects.filter(user_id = i.hall_no)
               rlang_pay  = Rlang.objects.filter(user_id = i.hall_no)
               rust_pay   = RUST.objects.filter(user_id = i.hall_no)
               swift_pay  = SWIFT.objects.filter(user_id = i.hall_no)
               cpplang_pay  = SWIFT.objects.filter(user_id = i.hall_no)
               
            return render (req , "college_search.html" , locals())

def clg_test_add(req):
     
     name = req.COOKIES['name']
     val_id = req.COOKIES['id']
     text = None
     college = College.objects.get(id =val_id)
     if req.method == "POST" :
        question = req.POST.get('name')
        a = req.POST.get('a')
        b = req.POST.get('b')
        c = req.POST.get('c')
        d= req.POST.get('d')
        ans = req.POST.get('ans')
        sub = req.POST.get('sub')
        data = Question(problem =question , a =a , b= b ,c= c , d =d ,ans= ans , sub = sub , uni= college.university , clg =college.clg_code )
        data.save()
        text = "Question is added to University database!"
        return render(req , "clg_test_add.html" , locals())
     return render(req , "clg_test_add.html" , locals())

def student_profile(req , num):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    college = College.objects.get(id =val_id)
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
    return render(req,"student_profile.html" , locals())

def clg_deep_result(req , sub , num):
     name = req.COOKIES['name']
     val_id = req.COOKIES['id']
     college = College.objects.get(id =val_id)
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
     
     return render(req,"clg_stu_results.html" , locals())

def clg_stu_lis_search(req):
   name = req.COOKIES['name']
   query = req.GET["search"]
   val_id = req.COOKIES['id']
   college = College.objects.get(id =val_id)
   print(query)
   if query != None:
            students = []
            val_id = req.COOKIES['id']
            data = Student.objects.filter(hall_no = query)
            print(data)
            text = "Student Not found!"
            for i in data:
                if i.clg_code ==  college.clg_code:
                     text = None
                     students.append(i)
            return render(req , "re_searcch_stu.html", locals())
    
def clg_profile(req):
   name = req.COOKIES['name']
   val_id = req.COOKIES['id']
   college = College.objects.get(id =val_id)
   return render(req, "clg_profile.html" , locals())

def clg_update_pro(req):
   name = req.COOKIES['name']
   val_id = req.COOKIES['id']
   college = College.objects.get(id =val_id)
   if req.method == "POST" :
         
         name = req.POST.get("name")
         hall = req.POST.get("hall")
         phno = req.POST.get("phno")
         clg = req.POST.get("clg")
         clg_code = req.POST.get("clg_code")
         uni = req.POST.get("uni")
         user  = req.POST.get("user")

         if req.FILES.get("pic") == None:
             pic = college.profile
         else:
             pic = req.FILES.get("pic")

         college.name = name
         college.contact = phno
         college.postal = hall
         college.city =  clg
         college.clg_code = clg_code
         college.university = uni
         college.principal = user
         college.profile = pic
         college.save()
   return render(req , "clg_pro_update.html",locals())

def clg_support(req):
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    user = College.objects.get(id = val_id)
    if req.method == "POST":
        title = req.POST.get('name')
        description = req.POST.get("description")
        data = CustomerSupport(name = name , title = title , by_from = "College" , emp_id = user.clg_code , description = description ,solution = False )
        data.save()
        msg = "we under stand your problem our member will respond as soon as possible!"
        

    
    return render(req,"clg_support.html" , locals())

def chat_clg(req):
    name = req.COOKIES.get('name')
    val_id = req.COOKIES.get('id')
    user = College.objects.get(id=val_id)
    chat = messsanger.objects.filter(sender_id = user.id , sender_type="college")

    return render(req,"clg_chat.html" ,locals())


def send_msg_clg(req):
    name = req.COOKIES.get('name')
    val_id = req.COOKIES.get('id')
    msg  = req.GET['msg']
    new = messsanger(name =name , msg = msg , sender_id = val_id , sender_type = "college" , created = "user")
    new.save()
    return redirect('chat_clg')

