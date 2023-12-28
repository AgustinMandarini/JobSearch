from .utils.scraper import find_jobs
from .models import IndeedJobs
from celery import shared_task


@shared_task
def update_jobs_schedule():

    print("Scrapping jobs...")
    newIndeedJobs = find_jobs("developer", "remote")
    print("Jobs scrapped successfully!")

    # First we delete all current jobs
    delete_all_indeed_jobs = IndeedJobs.objects.all()
    delete_all_indeed_jobs.delete()

    # Then we create new registries
    for indeedJob in newIndeedJobs:

        indeed_jobs = IndeedJobs(**indeedJob)

        # Save the indeed_jobs objects to the database
        indeed_jobs.save()

    print("Jobs updated successfully!")

    return "Indeed Jobs Updated!"
