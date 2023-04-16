from django.urls import path
from . import views
from rest_framework import routers
router = routers.SimpleRouter()
app_name = 'myadmin'

urlpatterns = [
    path('kc-admin-dashboard/', views.kc_admin_dashboard, name='kc-admin-dashboard'),
    path('kc-user/', views.kc_user,name='kc-user'),
    path('kc-admins/', views.kc_admins,name='kc-admins'),
    path('kc-colleges/', views.kc_colleges, name='kc-colleges'),
    path('kc-mailbox/', views.kc_mailbox, name='kc-mailbox'),
    path('kc-compose/', views.kc_compose,name='kc-compose'),
    path('kc-readmail/', views.kc_readmail, name='kc-readmail'),
    path('kc-coursecategory/', views.kc_coursecategory, name='kc-coursecategory'),
    path('kc-subcategory/',views.kc_subcategory, name='kc-subcategory'),
    # path('Register-college/', views.register_college),
    # path('Register-user/', views.register_user),
    # path('forgot-password/', views.forgot_password),
    # path('change-password/', views.change_password),
    # path('college-detail/', views.college_detail),
    # path('apply/', views.apply),
    # path('login/checkuser/', views.loginregister),
    # path('verify-otp/', views.verify_otp, name='verify_otp'),
]