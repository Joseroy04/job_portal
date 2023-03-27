from django.contrib import admin

# Register your models here.
from .models import job,jobmanager

admin.site.register(job)

from django.contrib import admin
from .models import Candidate, job, JobApplication

class JobApplicationInline(admin.TabularInline):
    model = JobApplication
    extra = 0

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'created_at', 'is_active')
    list_filter = ('created_at', 'is_active')
    search_fields = ('title', 'description', 'company', 'location')
    inlines = [JobApplicationInline]

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'phone', 'created_at')
    search_fields = ('user__username', 'name', 'email', 'phone')

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', )
    # list_filter = ('status', 'created_at')
    search_fields = ('candidate__user__username', 'candidate__name', 'job__title', 'job__company')

# admin.site.register(job, JobAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
