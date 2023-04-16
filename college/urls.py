from django.urls import path
from . import views
from rest_framework import routers
app_name = 'college'
router = routers.SimpleRouter()
router.register(r'college-basic-info', views.College_details_viewset,basename='College_details_viewset')


urlpatterns = [
    
]
urlpatterns += router.urls