"""
URL configuration for sattva project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import *
from super.views import *
from college.views import *
from user.views import *
from university.views import *
from django.conf import settings
from django.conf.urls.static import static
from employee.views import *

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),


    #universal links
    path('', login  , name="login"),
    path('signup/', signup  , name="signup"),
    path('signup-as/', signup_as  , name="signup_as"),
    path("signup/verifyemail/" , mail_verify , name="mail") ,
    path("login/otp-verification" , login_verify  , name="otp") ,
    path("settings/forgot-passkey/" , forgot , name="forgot" ),
    path("settings/login-unable/forgot-passkey/reset-password/<int:key>" , reset , name="reset" ),
    path("settings/forgot-passkey/updated", updatedpasskey , name="passkey_done"),
    path("settings/logout", logout , name="logout"),
    path("locked-screen/", lock_screen , name="lock_screen"),
    path("settings/chanage_passkey", chanage_passkey , name="chanage_passkey"),
    
    #user
    path("home", home , name="user_home"),
    path("test/" ,test , name="test"),
    path("test/payment" ,test_pay , name="test_pay"),
    path("test/result" ,test_result , name="test_result"),
    path("test/payment/done/<slug:trans_id>" ,test_pay_done , name="test_pay_done"),
    path("test/paid/setup/<slug:sub>/<int:num>" ,take_test_now,name="take_test" ),
    path("test/result/anylasisi/<slug:sub>/<int:num>" ,deep_result,name="deep_rusult" ),
    path("test/paid/setup/ongoing" ,test_ongoing,name="take_test_ongoing" ),
    path("settings/profile" ,user_profile,name="user_profile" ),
    path("settings/profile/update" ,update_user_profile,name="update_user_profile" ),
    path('video_feed', video_feed, name='video_feed'), #-> for camara setup
    path('video_feed/for/alerts', video_feed_alert, name='video_feed_alert'), #-> for camara alerts
    path("user/help-line/asking/for/help" , user_support,name="user_support" ),





    #college
    path("college/home", college_home , name="college_home"),
    path("college/students" ,students , name="students"),
    path("college/view/profile" ,clg_profile,name="clg_profile"),
    path("college/students/search" ,college_search , name="college_search"),
    path("college/add-question/touni" ,clg_test_add , name="clg_test_add"),
    path("college/student/profile/<int:num>" ,student_profile , name="student_profile"),
    path("college/student_search/student" ,clg_stu_lis_search , name="clg_stu_lis_search"),
    path("college/student/result/anylasisi/<slug:sub>/<int:num>" ,clg_deep_result,name="clg_stu_rusult" ),
    path("college/help-line/asking/for/help" , clg_support,name="clg_support" ),
    path("college/setting/profile/update" ,clg_update_pro,name="clg_upd_pro" ),


    #univesity
    path("university/home", uni_home , name="uni_home"),
    path("university/colleges" ,colleges , name="colleges"),
    path("university/search/college" , uni_search_clg , name="uni_search_clg"),
    path("university/college/search" ,uni_search , name="uni_search"),
    path("university/add-question/touni" ,uni_test_add , name="uni_test_add"),
    path("university/search/student" ,uni_search_stu , name="uni_search_stu"),
    path("university/college/students" ,uni_students , name="uni_stu"), 
    path("university/student/profile/<int:num>" ,student_profile_uni , name="student_profile_uni"),
    path("university/college/profile/<int:num>" ,clg_profile_uni , name="clg_profile_uni"),
    path("university/student/result/anylasisi/<slug:sub>/<int:num>" ,uni_deep_result,name="uni_stu_rusult" ),
    path("university/view/profile" ,uni_profile,name="uni_profile"),
    path("university/help-line/asking/for/help" , uni_support,name="uni_support" ),

    
    

    #super admin
    path("super-admin/home" , admin_home , name="super_admin_home"),
    path("super-admin/university-list" ,admin_uni, name="super_admin_uni"),
    path("super-admin/college-list" ,admin_clg, name="super_admin_clg"),
    path("super-admin/Student-list" ,admin_stu, name="super_admin_stu"),
    path("super-admin/college/search" ,admin_clg_search, name="admin_clg_search"),
    path("super-admin/student/search" ,admin_stu_search, name="admin_stu_search"),
    path("super-admin/student/details/<int:num>" ,student_profile_super, name="student_profile_super"),
    path("super-admin/college/details/<int:num>" ,clg_profile_super, name="clg_profile_super"),
    path("super-admin/student/result/anylasisi/<slug:sub>/<int:num>" ,super_deep_result,name="super_stu_rusult" ),
    path('super-admin/student/cheat-sheet/anylasisi/<slug:sub>/<int:num>', video_feed_VIDEO, name='images'), #-> for image show
    path('super-admin/admit/employes/to/work', add_emp , name='add_emp'), #-> for adding emplayes


    #employee  
    path("employee/home" , emp_home , name="emp_home"),
    path("employee/all/problems" , all_problems , name="all_problems"),
    path("employee/solution/for/problem/<int:num>" , sol_problems , name="sol_problem"),




]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
