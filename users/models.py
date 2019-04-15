from django.db import models

class Users(models.Model):
    user_first_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    login_name = models.CharField(max_length=10, null=False, blank=False)
    acc_password = models.CharField(max_length=30, null=False, blank=False)
