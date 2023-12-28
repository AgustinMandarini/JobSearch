from rest_framework import generics
from django.http import HttpResponse
from .models import IndeedJobs
from .serializers import JobsSerializer
from django_celery_beat.models import IntervalSchedule, PeriodicTask

# Lists all jobs saved on database


class ListJobs(generics.ListAPIView):

    serializer_class = JobsSerializer

    def get_queryset(self):
        # Utiliza una expresión regular para buscar coincidencias en los títulos

        # JUNIOR FILTER
        # Filtra con regex los resultados que contengan alguna de aquellas palabas
        queryset = IndeedJobs.objects.exclude(
            title__iregex=fr'.*(senior|sr|ssr|semi senior|ssr).*')

        return queryset

# Schedules intervals of jobs listing updates while implementing scraper script


def update_jobs_schedule(request):
    interval, _ = IntervalSchedule.objects.get_or_create(
        every=30,
        period=IntervalSchedule.MINUTES,
    )

    PeriodicTask.objects.create(
        interval=interval,
        name='update_jobs_schedule',
        task='api.tasks.update_jobs_schedule',
        # args=json.dumps([])
        # one_off=True
    )

    return HttpResponse("Jobs update scheduled!")
