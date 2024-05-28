from django.shortcuts import render , redirect
from super.models import *
from university.models import *
from college.models import *
from user.models import *
from employee.models import *
from.models import *

# Create your views here.
def emp_home(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    employee = Employ.objects.get(id=val_id)
    return render(req,"emp_home.html" ,locals())


def all_problems(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    employ = Employ.objects.get(id=val_id)
    problems = CustomerSupport.objects.all()
    return render(req,"all_emp_sol.html",locals())


def sol_problems(req , num):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    employ = Employ.objects.get(id=val_id)
    problem = CustomerSupport.objects.get(id=num)
    if req.method == "POST":
        solution = req.POST.get('solution')
        problem.solution = solution
        problem.save()
        return redirect("all_problems")
    return render(req,"sol_problem.html",locals())

def chat_emp(req):
    name  = req.COOKIES['name']
    val_id = req.COOKIES['id']
    employ = Employ.objects.get(id = val_id)

    student = Student.objects.all()
    college = College.objects.all()
    university = University.objects.all()

    return render(req,'emp_chat.html',locals())



def emp_chat_personal(req,type,id):
    name = req.COOKIES.get('name')
    val_id = req.COOKIES.get('id')
    employ = Employ.objects.get(id=val_id)

    student = Student.objects.all()
    college = College.objects.all()
    university = University.objects.all()

    if type == "university":
        data = University.objects.get(id=id)
        user_name = data.name
        location = data.city
    elif type == "college":
        data = College.objects.get(id=id)
        user_name = data.name
        location = data.city
    elif type == "student":
        data = Student.objects.get(id=id)
        user_name = data.name
        location = data.college

    chat = messsanger.objects.filter(sender_id = id , sender_type=type )
    return render(req, 'emp_chat_personal.html', locals())      

def send_msg_emp(req,type,id):

    if type == "university":
        data = University.objects.get(id=id)
        user_name = data.name
        location = data.city
    elif type == "college":
        data = College.objects.get(id=id)
        user_name = data.name
        location = data.city
    elif type == "student":
        data = Student.objects.get(id=id)
        user_name = data.name
        location = data.college

    msg  = req.GET['msg']
    print(msg)
    new = messsanger(name =user_name , msg = msg , sender_id = id , sender_type = type , created = "sender"  )
    new.save()
    print(new.name , new.sender_id , new.sender_type, new.created)
    return redirect('emp_chat_personal',type = type , id =id )



def vidoe_chat(req):
    name = req.COOKIES['name']
    val_id = req.COOKIES['id']
    employee = Employ.objects.get(id=val_id)
    return render(req,"video_chat.html",locals())



#                                         {% for i in chat %}
#                                         {% if i.created == "user"%}
#                                             <p>{{i.msg}}</p>
#                                         {% endif %}
#                                         {% if i.created == "sender"%}
#                                             <p>{{i.msg}}</p>
#                                         {% endif %}
#                                         {% endfor %}


    