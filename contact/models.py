from django.db import models

# Create your models here.

class BSc_Admission_Form(models.Model):
    fullname = models.CharField(max_length=50)
    image = models.ImageField(upload_to="BSc/BSC-image/")
    file = models.FileField(upload_to="BSc/BSC-PUC/")
    branch = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    adhar = models.FileField(upload_to="BSc/BSc-Adhar-File")

    def __str__(self):
        return self.fullname



from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    register_number = models.CharField(max_length=20)
    college_id = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='user/profile_pics/', default='profile_pics/default.jpg')

    def __str__(self):
        return self.user.username


class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming User is extended with Student profile
    subject = models.CharField(max_length=100)
    marks_obtained = models.FloatField()
    total_marks = models.FloatField()
    pass_status = models.BooleanField()

    def __str__(self):
        return f"{self.student.username} - {self.subject}"
    

class UG_Course(models.Model):
    name = models.CharField(max_length=100)
    branches = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    fees = models.CharField(max_length=50)

    class Meta:
        db_table = "ug_courses"  
        

    def __str__(self):
        return self.name
    

class UG_Study(models.Model):
    bsc = models.FileField(upload_to='bsc_papers')
    bca = models.FileField(upload_to='bca_papers',default='bca_papers/default_bca.pdf')
    bcom = models.FileField(upload_to='bcom_papers',default='bcom_papers/default_bcom.pdf')
    ba = models.FileField(upload_to='ba_papers',default='ba_papers/default_ba.pdf')

class Notification(models.Model):
    notification_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.notification_name


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.title