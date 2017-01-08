from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from decimal import Decimal
# Create your models here.
class student_information(models.Model):
    CSE = 'C'
    ECE = 'E'
    IT = 'I'
    EEE = 'E'
    WISE = 'W'
    ATL = 'A'
    MISSION_RANDD = 'M'
    IOT = 'IOT'
    TOASTMASTER = 'T'

    BRANCH = (
        (CSE, 'cse'),
        (ECE, 'ece'),
        (IT, 'it'),
        (EEE, 'eee'),
    )
    ACTIVITIES = (
        (WISE, 'WISE'),
        (ATL, 'ATL'),
        (MISSION_RANDD, 'Mission R & D'),
        (IOT, 'IOT'),
        (TOASTMASTER, 'Toast Master Club'),

    )
    

    
    full_name = models.CharField(max_length = 50)
    roll_number = models.CharField(max_length = 20)
    branch = models.CharField(max_length = 2, choices = BRANCH, default = CSE,)
    emailid = models.CharField(max_length = 100)
    dob = models.CharField(max_length = 20)
    aggregate = models.DecimalField(max_digits = 3, decimal_places = 2)
    activities = models.CharField(max_length = 2, choices = ACTIVITIES,)
    certifications = models.CharField(max_length = 2000)
    def __str__(self):
        return '%s %s %s %s %s %d %s %s' % (self.full_name, self.roll_number, self.branch, self.emailid, self.dob, self.aggregate, self.activities, self.certifications)


