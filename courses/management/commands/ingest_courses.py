from datetime import datetime
import json

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from courses.models import Course

class Command(BaseCommand):
    help = 'Create courses from JSON file'

    def handle(self, *args, **kwargs):
        # set the path to the datafile
        datafile = settings.BASE_DIR / 'data' / 'courses.json'
        assert datafile.exists()

        # load the datafile
        with open(datafile, 'r') as f:
            data = json.load(f)
        
        # create tz-aware datetime object from the JSON string.
        DATE_FMT = "%Y-%m-%d %H:%M:%S"
        for course in data:
            course_pub_date = datetime.strptime(course['course_pub_date'], DATE_FMT)
            course['course_pub_date'] = make_aware(course_pub_date)

        # convert list of dictionaries to list of course models, and bulk_create
        courses = [Course(**course) for course in data]

        Course.objects.bulk_create(courses)