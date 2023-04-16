from django.db import models
import uuid
from mainapp.models import RegisteredCollege, RegisteredUsers

YES_OR_NO_CHOICE =(
    ('Yes','Yes'),
    ('No','No')
)
# Create your models here.
class CollegeBasicInfo(models.Model):
    ids = models.UUIDField(default=uuid.uuid4,primary_key=True)
    college = models.ForeignKey(RegisteredCollege, on_delete=models.CASCADE)
    info = models.TextField()
    affiliations = models.TextField()
    incorporation_year = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.college.name)
    
class CollegeAffiliation(models.Model):
    ids = models.UUIDField(default=uuid.uuid4,primary_key=True)
    college = models.ForeignKey(RegisteredCollege, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    url = models.CharField(max_length=500, null=True)
    year = models.CharField(max_length=20)
    organizer = models.CharField(max_length=300)
    title = models.CharField(max_length=400)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.college.name)

class collegeCoursers(models.Model):
    ids = models.UUIDField(default=uuid.uuid4,primary_key=True)
    college = models.ForeignKey(RegisteredCollege, on_delete=models.CASCADE)
    course = models.CharField(max_length=200)
    adminssion_process = models.TextField()
    ten_marks = models.CharField(max_length=20)
    twelve_mark = models.CharField(max_length=20)
    graduation_mark = models.CharField(max_length=20)
    course_duration = models.IntegerField(max_length=20)
    total_fee = models.IntegerField(max_length=30)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.college.name)

class CollegeInfrastructure(models.Model):
    ids = models.UUIDField(default=uuid.uuid4, primary_key=True)
    college = models.ForeignKey(RegisteredCollege, on_delete=models.CASCADE)
    library = models.CharField(max_length=10, choices=YES_OR_NO_CHOICE, default='No')
    library_details = models.TextField()
    labs = models.CharField(max_length=10, choices=YES_OR_NO_CHOICE, default='No')
    lab_details = models.TextField()
    medicals = models.CharField(max_length=10, choices=YES_OR_NO_CHOICE, default='No')
    medical_details = models.TextField()
    wifi = models.CharField(max_length=10, choices=YES_OR_NO_CHOICE, default='No')
    auditorim = models.CharField(max_length=10, choices=YES_OR_NO_CHOICE, default='No')
    auditorim_detais = models.TextField()
    sport = models.CharField(max_length=10, choices=YES_OR_NO_CHOICE, default='No')
    sport_details = models.TextField()
    hostel = models.CharField(max_length=10, choices=YES_OR_NO_CHOICE, default='No')
    hostel_details = models.TextField()
    other = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.college.name)

class CollegePlacementDetails(models.Model):
    ids = models.UUIDField(default=uuid.uuid4, primary_key=True)
    course = models.CharField(max_length=300)
    total_student = models.IntegerField(default=0, max_length=20)
    total_recruiter = models.IntegerField(default=0, max_length=20)
    total_student_place = models.IntegerField(default=0, max_length=20)
    average_package = models.FloatField(default=0.0, max_length=20)
    year = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.course)+'-'+str(self.year)



