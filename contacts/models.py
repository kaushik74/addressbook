from django.db import models

from users.models import Users

class Contacts(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,null=False, blank=False)
    last_name = models.CharField(max_length=30,null=True, blank=True)
    gender = models.CharField(max_length=10,null=False, blank=False)
    address = models.CharField(max_length=500,null=False, blank=False)
    city = models.CharField(max_length=30,null=False, blank=False)
    state = models.CharField(max_length=30,null=False, blank=False)
    zipcode = models.CharField(max_length=10,null=False, blank=False)
    email = models.EmailField()
    mobile_no = models.IntegerField(null=True)
    phone_no = models.IntegerField(blank=True,null=True)
    date_of_birth = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

