from rest_framework import serializers
from .models import IndeedJobs


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndeedJobs
        fields = ('id', 'title', 'job_url', 'job_id',
                  'company', 'location', 'date', 'salary')
