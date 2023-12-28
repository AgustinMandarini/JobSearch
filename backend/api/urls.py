from django.urls import path
from .views import ListJobs

urlpatterns = [
    path('', ListJobs.as_view())

]
