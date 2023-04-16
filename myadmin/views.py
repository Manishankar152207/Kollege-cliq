import re
from urllib import request
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect
import copy
import uuid
from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import base64
import string
import random
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

def kc_admin_dashboard(request):
    return render(request, 'dashboard/index.html')

def kc_user(request):
    return render(request, 'dashboard/user.html')

def kc_admins(request):
    return render(request, 'dashboard/admins.html')

def kc_colleges(request):
    return render(request, 'dashboard/colleges.html')

def kc_mailbox(request):
    return render(request, 'dashboard/mailbox.html')

def kc_compose(request):
    return render(request, 'dashboard/compose.html')

def kc_readmail(request):
    return render(request, 'dashboard/read-mail.html')

def kc_coursecategory(request):
    return render(request, 'dashboard/coursecategory.html')

def kc_subcategory(request):
    return render(request, 'dashboard/subcategory.html')