from django.db import models

# Create your models here.

class jobmanager(models.Manager):
    def sort_by_date(x):
        return x.order_by('-published_date')

class job(models.Model):
    # exp_ch =[ 
    #     ('Select experience', 'Select experience'),
    #     ('0','0'), #(value,label)
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('3+', '3+')
    # ]

    # location_ch=[
    #     ('Select job location', 'Select job location'),
    #     ('Mumbai','Mumbai'),
    #     ('Pune','Pune'),
    #     ('Navi mumbai','Navi Mumbai'),
    #     ('Thane','Thane'),
    #     ('Andheri','Andheri')
    # ]

    # job_cat = [
    #     ('Select job category', 'Select job category'),
    #     ('Entry Level','Entry-Level'),
    #     ('Mid level','Mid-Level'),
    #     ('Senior Level','Senior-Level')
    # ]

    # job_role = [
    #     ('Select job role', 'Select job role'),
    #     ('App developer','App developer'), 
    #     ('Database administrator','Database administrator'), 
    #     ('Service desk analyst','Service desk analyst'), 
    #     ('Software developer','Software developer'), 
    #     ('Software engineer','Software engineer'), 
    #     ('Software tester','Software tester'), 
    #     ('Web developer','Web developer') 
    # ]

    # job_degree = [
    #     ('Select degree', 'Select degree'),
    #     ('Any Degree','Any Degree'),
    #     ('M.E/M.Tech/M.S','M.E/M.Tech/M.S'),
    #     ('B.E/B.Tech','B.E/B.Tech'),
    #     ('MBA','MBA'),
    #     ('Diploma','Diploma'),
    # ]
    
    job_id = models.CharField(max_length=10)
    # role = models.CharField(default=job_role, max_length=50, choices=job_role)
    job_role = models.CharField( max_length=50)
    drive_company_name = models.CharField(max_length=50)
    # company_site = models.URLField(max_length=200)
    job_category = models.CharField(max_length=50,)
    # salary = models.FloatField()
    # yop = models.CharField(max_length=50)
    # job_location = models.CharField(max_length=50, choices=location_ch, default=location_ch)
    job_location = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    # qualification = models.CharField(max_length=50, choices=job_degree, default=job_degree)
    #specialization = models.CharField(max_length=50, choices=)
    vacancies = models.IntegerField()
    experience = models.CharField(max_length=50)
    # experience = models.CharField(max_length=50, choices=exp_ch, default=exp_ch)
    # drive_location = models.CharField(max_length=100)
    venue_details = models.TextField(max_length=200, blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    # last_date = models.DateField()
    # apply_link = models.URLField(max_length=200)
    last_modified = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()
    jb_manager = jobmanager()
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.job_id+"  "+self.job_role

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'jobDetails'
        verbose_name_plural = 'jobDetailss'
        
    
from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # resume = models.FileField(upload_to='resumes/')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import User

# class Job(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     employer = models.ForeignKey(User, on_delete=models.CASCADE)
#     posted_date = models.DateTimeField(auto_now_add=True)
#     deadline = models.DateField()
#     is_active = models.BooleanField(default=True)

job_status = [
        ('Pending','Pending'),
        ('Accept', 'Accept'),
        ('Reject','Reject')
    ]
class JobApplication(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(job, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    is_accepted = models.CharField(max_length=50,choices=job_status,default=job_status[0])
