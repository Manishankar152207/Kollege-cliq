from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect
import copy
import uuid
from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import BadRequest
import base64
import string
import random
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.response import Response
from college.serializer import CollegeBasicInfoSerializer, CollegeCourseFeeSerailizer, collegeAchivementSerializer,CollegeInfrastructerserializer
import json
from college.models import CollegeBasicInfo, collegeCoursers,CollegeInfrastructure, CollegeAffiliation
# Create your views here.

class College_details_viewset(viewsets.ViewSet):
    
    def create(self,request):
        data = request.POST
        try:
            college_id = data['college_ids']
        except Exception as e:
            raise BadRequest('college_id key is missing !!!')
        if CollegeBasicInfo.objects.filter(college__user_id=uuid.UUID(college_id)).exists():
            info_obj = CollegeBasicInfo.objects.get(college__user_id=uuid.UUID(college_id))
            serialized_data = CollegeBasicInfoSerializer(info_obj,data)
            serialized_data.is_valid(raise_exception=True)
            serialized_data.save()
        else:
            serialized_data = CollegeBasicInfoSerializer(data=data)
            serialized_data.is_valid(raise_exception=True)
            serialized_data.save()

        return JsonResponse({'message':'success','data':'information is updated successfully'})
    
    def list(self,request):
        return JsonResponse({'message':'list operations'})

    @action(detail=False)
    def course_fee(self, request):
        data = request.GET
        try:
            college_id = data['college_ids']
            ids = data['ids']
        except Exception as e:
            raise BadRequest('college_id or ids  key is missing !!!')
        if ids :
            if collegeCoursers.objects.filter(ids=ids).exists():
                course_obj = collegeCoursers.objects.get(ids=uuid.UUID(ids))
                serialized_data = CollegeCourseFeeSerailizer(course_obj,data)
                serialized_data.is_valid(raise_exception=True)
                serialized_data.save()
        else:
            serialized_data = CollegeCourseFeeSerailizer(data=data)
            serialized_data.is_valid(raise_exception=True)
            serialized_data.save()
        return JsonResponse({'message':'success','data':'college fee and course is updated successfully'})

    @action(detail=False)
    def affiliaztions(self,request):
        data = request.GET
        try:
            college_id = data['college_ids']
            ids = data['ids']
        except Exception as e:
            raise BadRequest('college_id key is missing !!!')
        if ids:
            if CollegeAffiliation.objects.filter(ids=uuid.UUID(ids)).exists():
                affiliation_obj = CollegeAffiliation.objects.get(ids=uuid.UUID(ids))
                serialized_data = collegeAchivementSerializer(affiliation_obj,data)
                serialized_data.is_valid(raise_exception=True)
                serialized_data.save()
        else:
            serialized_data = collegeAchivementSerializer(data=data)
            serialized_data.is_valid(raise_exception=True)
            serialized_data.save()
        return JsonResponse({'message':'success','data':'college fee and course is updated successfully'})

    @action(detail=False)
    def placement_details(self,request):
        data = request.GET
        try:
            college_id = data['college_ids']
            ids = data['ids']
        except Exception as e:
            raise BadRequest('college_id key is missing !!!')
        if ids:
            if CollegeAffiliation.objects.filter(ids=uuid.UUID(ids)).exists():
                affiliation_obj = CollegeAffiliation.objects.get(ids=uuid.UUID(ids))
                serialized_data = collegeAchivementSerializer(affiliation_obj,data)
                serialized_data.is_valid(raise_exception=True)
                serialized_data.save()
        else:
            serialized_data = collegeAchivementSerializer(data=data)
            serialized_data.is_valid(raise_exception=True)
            serialized_data.save()
        return JsonResponse({'message':'success','data':'college fee and course is updated successfully'})

    @action(detail=False)
    def infrastructer(self,request):
        data = request.GET
        try:
            college_id = data['college_ids']
            ids = data['ids']
        except Exception as e:
            raise BadRequest('college_id key is missing !!!')
        if ids:
            if CollegeInfrastructure.objects.filter(ids=uuid.UUID(ids)).exists():
                affiliation_obj = CollegeInfrastructure.objects.get(ids=uuid.UUID(ids))
                serialized_data = CollegeInfrastructerserializer(affiliation_obj,data)
                serialized_data.is_valid(raise_exception=True)
                serialized_data.save()
        else:
            serialized_data = CollegeInfrastructerserializer(data=data)
            serialized_data.is_valid(raise_exception=True)
            serialized_data.save()
        return JsonResponse({'message':'success','data':'college fee and course is updated successfully'})





