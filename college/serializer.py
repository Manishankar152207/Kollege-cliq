
from rest_framework import serializers
from traitlets import default
from django.core.exceptions import BadRequest
from mainapp.models import RegisteredUsers,Contact,RegisteredCollege
import uuid
from college.models import CollegeBasicInfo, CollegeAffiliation, collegeCoursers, CollegeInfrastructure, CollegePlacementDetails

class CollegeBasicInfoSerializer(serializers.Serializer):
    info = serializers.CharField(required=True)
    affiliations= serializers.CharField(required=False)
    incorporation_year = serializers.CharField(required=False)
    college_ids = serializers.CharField(required=True)

    def create(self,validated_data):
        college_ids = validated_data.pop('college_ids')

        if college_ids:
            college_obj = RegisteredCollege.objects.get(user_id=college_ids)
            validated_data.update({'college':college_obj})
            return CollegeBasicInfo.objects.create(**validated_data)
        else:
            raise BadRequest('Invalid college ids ')
    
    def update(self,instance,validated_data):
        instance.info = validated_data.get('info',instance.info)
        instance.affiliations = validated_data.get('affiliations', instance.affiliations)
        instance.incorporation_year = validated_data.get('incorporation_year', instance.incorporation_year)

        instance.save()
        return instance
class CollegeCourseFeeSerailizer(serializers.Serializer):
    college_ids = serializers.CharField(required=True)
    course = serializers.CharField(max_length=200)
    adminssion_process = serializers.CharField()
    ten_marks = serializers.CharField(max_length=200)
    twelve_mark = serializers.CharField(max_length=200)
    graduation_mark = serializers.CharField(max_length=200)
    course_duration = serializers.CharField(max_length=100)
    total_fee = serializers.IntegerField()

    def create(self,validated_data):
        college_ids = validated_data.pop('college_ids')
        if college_ids:
            college_obj = RegisteredCollege.objects.get(user_id=college_ids)
            validated_data.update({'college':college_obj})
            return collegeCoursers.objects.create(**validated_data)
        else:
            raise BadRequest('invalid colleges ids or college_ids key is not provided in api call')
    def update(self,instance,validate_data):
        instance.course = validate_data.get('course', instance.course)
        instance.adminssion_process = validate_data.get('adminssion_process', instance.adminssion_process)
        instance.ten_marks = validate_data.get('ten_marks', instance.ten_marks)
        instance.twelve_mark = validate_data.get('twelve_mark', instance.twelve_mark)
        instance.graduation_mark = validate_data.get('graduation_mark', instance.graduation_mark)
        instance.course_duration = validate_data.get('course_duration', instance.course_duration)
        instance.total_fee = validate_data.get('total_fee', instance.total_fee)
        instance.save()
        return  instance
class collegeAchivementSerializer(serializers.Serializer):
    college_ids = serializers.CharField(required=True)
    name = serializers.CharField(max_length=400)
    url = serializers.CharField(max_length=500,required=False, allow_null=True, allow_blank=True)
    year = serializers.CharField(max_length=20)
    organizer = serializers.CharField(max_length=300)
    def create(self,validated_data):
        college_ids = validated_data.pop('college_ids')
        if college_ids:
            college_obj = RegisteredCollege.objects.get(user_id=college_ids)
            validated_data.update({'college':college_obj})
            return CollegeAffiliation.objects.create(**validated_data)
        else:
            raise BadRequest('invalid colleges ids or college_ids key is not provided in api call')
    def update(self,instance,validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.url = validate_data.get('url', instance.url)
        instance.year = validate_data.get('year', instance.year)
        instance.organizer = validate_data.get('organizer', instance.organizer)
        instance.save()
        return  instance

class CollegePlacementSerializer(serializers.Serializer):
    college_ids = serializers.CharField(required=True)
    course = serializers.CharField(max_length=400)
    total_student = serializers.IntegerField(default=0)
    total_recruiter = serializers.IntegerField(default=0)
    total_student_place = serializers.IntegerField(default=0)
    average_package = serializers.FloatField(default=0.0)
    year = serializers.CharField(max_length=30)

    def create(self,validated_data):
        college_ids = validated_data.pop('college_ids')
        if college_ids:
            college_obj = RegisteredCollege.objects.get(user_id=college_ids)
            validated_data.update({'college':college_obj})
            return CollegePlacementDetails.objects.create(**validated_data)
        else:
            raise BadRequest('invalid colleges ids or college_ids key is not provided in api call')
    def update(self,instance,validate_data):
        instance.course = validate_data.get('course', instance.course)
        instance.total_student = validate_data.get('total_student', instance.total_student)
        instance.total_recruiter = validate_data.get('total_recruiter', instance.total_recruiter)
        instance.total_student_place = validate_data.get('total_student_place', instance.total_student_place)
        instance.average_package = validate_data.get('average_package', instance.average_package)
        instance.year = validate_data.get('year', instance.year)
        instance.save()
        return  instance

class CollegeInfrastructerserializer(serializers.Serializer):
    college_ids = serializers.CharField(required=True)
    library = serializers.CharField(max_length=10, allow_null=True, allow_blank=True)
    library_details = serializers.CharField(allow_null=True, allow_blank=True)
    labs = serializers.CharField(allow_null=True, allow_blank=True)
    lab_details = serializers.CharField(allow_null=True, allow_blank=True)
    medicals = serializers.CharField(allow_null=True, allow_blank=True)
    medical_details = serializers.CharField(allow_null=True, allow_blank=True)
    wifi = serializers.CharField(allow_null=True, allow_blank=True)
    auditorim = serializers.CharField(allow_null=True, allow_blank=True)
    auditorim_detais = serializers.CharField(allow_null=True, allow_blank=True)
    sport = serializers.CharField(allow_null=True, allow_blank=True)
    sport_details = serializers.CharField(allow_null=True, allow_blank=True)
    hostel = serializers.CharField(allow_null=True, allow_blank=True)
    hostel_details = serializers.CharField(allow_null=True, allow_blank=True)
    other = serializers.CharField(allow_null=True, allow_blank=True)

    def create(self,validated_data):
        college_ids = validated_data.pop('college_ids')
        if college_ids:
            college_obj = RegisteredCollege.objects.get(user_id=college_ids)
            validated_data.update({'college':college_obj})
            return CollegeInfrastructure.objects.create(**validated_data)
        else:
            raise BadRequest('invalid colleges ids or college_ids key is not provided in api call')
    def update(self,instance,validate_data):
        instance.library = validate_data.get('library', instance.library)
        instance.library_details = validate_data.get('library_details', instance.library_details)
        instance.labs = validate_data.get('labs', instance.labs)
        instance.lab_details = validate_data.get('lab_details', instance.lab_details)
        instance.medicals = validate_data.get('medicals', instance.medicals)
        instance.medical_details = validate_data.get('medical_details', instance.medical_details)
        instance.wifi = validate_data.get('wifi', instance.wifi)
        instance.auditorim = validate_data.get('auditorim', instance.auditorim)
        instance.auditorim_detais = validate_data.get('auditorim_detais', instance.auditorim_detais)
        instance.sport = validate_data.get('sport', instance.sport)
        instance.sport_details = validate_data.get('sport_details', instance.sport_details)
        instance.hostel = validate_data.get('hostel', instance.hostel)
        instance.hostel_details = validate_data.get('hostel_details', instance.hostel_details)
        instance.other = validate_data.get('other', instance.other)
        instance.save()
        return  instance

