from django.shortcuts import render, redirect
from .models import JobApplication


def add_job_application(request):

    if request.method == "POST":
        company = request.POST.get("company")
        job_title = request.POST.get("job_title")
        job_id = request.POST.get("job_id")
        location = request.POST.get("location")
        application_date = request.POST.get("job_date")
        status = request.POST.get("status")
        job_url = request.POST.get("job_url")
        source = request.POST.get("source")
        notes = request.POST.get("notes")

        JobApplication.objects.create(
            company=company,
            job_title=job_title,
            job_id=job_id,
            location=location,
            application_date=application_date,
            status=status,
            job_url=job_url,
            source=source,
            notes=notes,
        )

        return redirect(add_job_application)

    return render(request, "application/add_job.html")


def edit_applications(request):
    applications = JobApplication.objects.all()

    search = request.GET.get("search", "")
    status = request.GET.get("status", "")

    if search:
        applications = applications.filter(company__icontains=search) | applications.filter(job_title__icontains=search)
    if status:
        applications = applications.filter(status=status)
    return render(
        request,
        "application/edit_job.html",
        {
            "applications": applications,
            "search": search,
            "status": status,

        }
    )


def edit_application(request, id):
    application = JobApplication.objects.get(id=id)

    if request.method == "POST":
        application.company = request.POST.get("company")
        application.job_title = request.POST.get("job_title")
        application.job_url = request.POST.get("job_url")
        application.status = request.POST.get("status")

        application.save()

        return redirect("edit_applications")

    return render(
        request,
        "application/edit_application.html",
        {"application": application}
    )


def delete_application(request, id):
    application = JobApplication.objects.get(id=id)

    application.delete()

    return redirect("edit_applications")

'''def search_application(request):
    application = JobApplication.objects.all().order_by("-id")

    search = request.GET.get("search", "")
    status = request.GET.get("status", "")

    if search:
        applications = application.filter(company_contains=search) | applications.filter(job_title=search)
    if status:
        applications = application.filter(status=status)

    return render(
        request,"application/search_application",{
            "application" : application,
            "search" : search,
            "status" : status,
        }
    )'''