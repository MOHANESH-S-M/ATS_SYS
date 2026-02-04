from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .forms import ApplicationForm ,AtsAnalyseForm
from .models import Application
from hr.models import jobpost
from django.contrib import messages
from django.core.mail import send_mail
from .utils import score_resume
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# this is for job apply
def apply_to_job(request,slug):
    job = get_object_or_404(jobpost,slug=slug)
    if job.is_expired():
        return render(request,'applicants/job_expired.html',{"job":job})
    if request.method == "POST":
        form = ApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(request,"Application Submitted Successfully")
            return redirect('apply-success')
    else:
        form = ApplicationForm()
    return render(request,"applicants/apply_form.html",{"form":form ,"job":job})
# This is only to produce success
def apply_success(request):
    return render(request ,'applicants/apply_success.html')

# logic to analyse ats
def ats_analyse_views(request,job_id):
    job = get_object_or_404(jobpost,id = job_id)
    applicants = Application.objects.filter(job=job)
    
    if request.method == "POST":
        form = AtsAnalyseForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data["num_to_shortlist"]
            jd = job.description

            scored =[]

            for app in applicants:
                if app.resume:
                    score = score_resume(app.resume.path,jd)
                    app.ats_score = score

                    scored.append(app)
            # for sorting and updation
            print( "this is ",scored)
            scored.sort(key=lambda x : x.ats_score , reverse= True)
            sortlisted = scored[:num]
            rejected = scored[num:]

            for app in sortlisted:
                app.status = 'shortlisted'
                app.save()
                send_mail("You're Shortlisted! ", "Congrats! this is the mail,sent to you for testing purposes", "hr@example.com", [app.email])
            


            for app in rejected:
                app.status = 'rejected'
                app.save()
                send_mail("Application Update", "Thank you, but not selected.  this is the mail,sent to you for testing purposes", "hr@example.com", [app.email])

            print("Mail sent")

            """print("those who are sort listed",sortlisted)
            print("those who are rejected listed",rejected)
            return HttpResponse(f"the sortlisted applicants {sortlisted} , the rejected applicants{rejected}")"""
            return redirect("mail-sent")

    else:
        form = AtsAnalyseForm()
    return render(request,'applicants/ats_form.html',{"form":form , "job":job})

def mail_sent(request):
    return render(request,"applicants/Mailsent.html")