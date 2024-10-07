from django.contrib import admin
from contact.models import BSc_Admission_Form,Student,Result,UG_Course,UG_Study,Notification,Gallery

# Register your models here.

class BSc_Admission_Form_Admin(admin.ModelAdmin):
    list_disp = ('fullname','image','file','branch','father_name','date_of_birth','gender','caste','mobile','email','adhar')

admin.site.register(BSc_Admission_Form, BSc_Admission_Form_Admin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'register_number', 'college_id')
    search_fields = ('user__username', 'register_number', 'college_id')

admin.site.register(Student, StudentAdmin)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks_obtained', 'total_marks', 'pass_status')

@admin.register(UG_Course)
class UG_CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'branches', 'duration', 'eligibility')

admin.site.register(UG_Study)
admin.site.register(Notification)
admin.site.register(Gallery)