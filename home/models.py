# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Commercial Manage(models.Model):

    #__Commercial Manage_FIELDS__
    influencer name = models.CharField(max_length=255, null=True, blank=True)
    influencer number = models.IntegerField(null=True, blank=True)
    share count = models.IntegerField(null=True, blank=True)
    visiable count = models.IntegerField(null=True, blank=True)

    #__Commercial Manage_FIELDS__END

    class Meta:
        verbose_name        = _("Commercial Manage")
        verbose_name_plural = _("Commercial Manage")



#__MODELS__END
