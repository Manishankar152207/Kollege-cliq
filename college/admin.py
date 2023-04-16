from django.contrib import admin
from college.models import *
# Register your models here.
@admin.register(CollegeBasicInfo)
class InfoRegisteredUsers(admin.ModelAdmin):
    pass

@admin.register(CollegeAffiliation)
class InfoRegisteredCollege(admin.ModelAdmin):
    pass

@admin.register(collegeCoursers)
class InfoContact(admin.ModelAdmin):
    pass

@admin.register(CollegeInfrastructure)
class InfoRegisteredUsers(admin.ModelAdmin):
    pass

@admin.register(CollegePlacementDetails)
class InfoRegisteredCollege(admin.ModelAdmin):
    pass
