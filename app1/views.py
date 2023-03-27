from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.forms import jobapply
from app1.models import job
#import datetim
from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def index(request):
    content = {}
    content['data'] = job.objects.all()
    return render(request,'index.html', content)

@staff_member_required(login_url="index")
def add_job(request):
    now = datetime.now()
    
    if request.method == 'POST':
        fm = jobapply(request.POST)
        if fm.is_valid():
            # print(fm)
            # fm.save()
            j1 = fm.save(commit=False)
            j1.last_modified = now
            j1.save()
            #fm.save_m2m()
            return redirect('/alljob')
    else:
        fm = jobapply()
    return render(request, "addjob.html", {'form':fm})


@staff_member_required(login_url="index")
def edit_job(request, rid):
    now = datetime.now()
    # format = '%Y-%m-%d %H:%M %p'
    # d1 = now.strftime(format)

    j1 = job.objects.get(id=rid)
    if request.method == 'POST':
        fm  = jobapply(request.POST, instance=j1)
        if fm.is_valid():
            #fm.save()
            j2 = fm.save(commit=False)
            j2.last_modified = now
            j2.save()
            return redirect('/alljob')
    else:
        fm = jobapply(instance=j1)
    return render(request, 'edit_job.html', {'form': fm})

def get_job(request, rid):
    content = {}
    content['data'] = job.objects.get(id=rid)
    return render(request, 'getjob.html',content)

def search_job(request):
    content = {}
    content['data'] = job.objects.all()
    return render(request, 'searchjob.html',content)

@staff_member_required(login_url="index")
def delete_job(request, rid):
    x = job.objects.get(id=rid)
    x.delete()
    return redirect('/alljob')

def view_all_jobs(request):
    content = {}
    content['data'] = job.objects.all()
    return render(request, 'dashboard.html',content)

def filterbybatch(request):
    if request.method == "GET":
        st=request.GET.get('batch')
        if st != None:
            content = {}
            content['data'] = job.objects.filter(yop__icontains=st)
    return render(request, 'searchjob.html',content)

def filterbylocation(request):
    if request.method == "GET":
        st=request.GET.get('joblocation')
        if st != None:
            content = {}
            content['data'] = job.objects.filter(job_location__icontains=st)
    return render(request, 'searchjob.html',content)

def filterbydegree(request):
    if request.method == "GET":
        st=request.GET.get('degree')
        if st != None:
            content = {}
            content['data'] = job.objects.filter(qualification__icontains=st)
    return render(request, 'searchjob.html',content)

def sortbydate(request):
    content = {}
    content['data'] = job.jb_manager.sort_by_date()
    return render(request, 'searchjob.html',content)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



##########
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login
# from app1.forms import CandidateSignUpForm
# from app1.models import Candidate

# def candidate_signup(request):
#     if request.method == 'POST':
#         form = CandidateSignUpForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             # user.candidate.resume = form.cleaned_data.get('resume')
#             user.candidate.name = form.cleaned_data.get('name')
#             user.candidate.email = form.cleaned_data.get('email')
#             user.candidate.phone = form.cleaned_data.get('phone')
#             user.candidate.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = CandidateSignUpForm()
#     return render(request, 'candidate_signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from app1.forms import CandidateSignUpForm
from app1.models import Candidate

def candidate_signup(request):
    if request.method == 'POST':
        form = CandidateSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            if not hasattr(user, 'candidate'):
                Candidate.objects.create(user=user, name=name, email=email, phone=phone)
            else:
                candidate = user.candidate
                candidate.name = name
                candidate.email = email
                candidate.phone = phone
                candidate.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = CandidateSignUpForm()
    return render(request, 'candidate_signup.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from app1.forms import CandidateLoginForm

def candidate_login(request):
    if request.method == 'POST':
        form = CandidateLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active :
                    login(request, user)
                    return redirect('index')
                else:
                    form.add_error(None, 'Invalid login credentials')
            else:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = CandidateLoginForm()
    return render(request, 'candidate_login.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app1.models import job, Candidate, JobApplication
# from .forms import JobApplicationForm

def job_list(request):
    jobs = job.objects.filter(is_active=True).order_by('-posted_date')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

from django.http import HttpResponseRedirect
@login_required(login_url="candidate_login")
def apply_for_job(request, job_id):
    jobObject = get_object_or_404(job, job_id=job_id)
    candidate = get_object_or_404(Candidate, user=request.user)
    # form = JobApplicationForm(request.POST or None) 
    # if request.method == 'POST':
        # if form.is_valid():
    JobApplication.objects.get_or_create(candidate=candidate,job=jobObject,application_date=datetime.today())
        # application = form.save(commit=False)
        # application.job = job
        # application.candidate = candidate
        # application.save()
    return redirect('job_applications')
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return render(request, 'apply_for_job.html', {'job': job, 'form': form})

@login_required(login_url="candidate_login")
def job_applications(request):
    candidate = get_object_or_404(Candidate, user=request.user)
    applications = JobApplication.objects.filter(candidate=candidate).order_by('-application_date')
    return render(request, 'job_applications.html', {'applications': applications})

@login_required(login_url="candidate_login")
def accept_job_application(request, application_id):
    application = get_object_or_404(JobApplication, pk=application_id)
    if request.user == application.job.employer:
        application.is_accepted = True
        application.save()
    return redirect('job_applications')

@login_required(login_url="candidate_login")
def reject_job_application(request, application_id):
    application = get_object_or_404(JobApplication, pk=application_id)
    if request.user == application.job.employer:
        application.is_accepted = False
        application.save()
    return redirect('job_applications')

@login_required(login_url="candidate_login")
def candidate_logout(request):
    logout(request)
    return redirect('index')