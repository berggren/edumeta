from django.db import models
from django.db.models.aggregates import Sum

class Institution(models.Model):
    realm = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    type = models.IntegerField()
    org_name_se = models.CharField(max_length=255, null=True, blank=True)
    org_name_en = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    info_url_se = models.URLField(null=True, blank=True)
    info_url_en = models.URLField(null=True, blank=True)
    policy_url_se = models.URLField(null=True, blank=True)
    policy_url_en = models.URLField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % self.org_name_en
    def get_locations(self):
        return Location.objects.filter(institution=self)
    def get_contacts(self):
        return Contact.objects.filter(institution=self)
    def get_ap_count(self):
        return Location.objects.filter(institution=self).aggregate(Sum('ap_no'))['ap_no__sum']
    class Admin:
        pass

class Contact(models.Model):
    institution = models.ForeignKey(Institution)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % self.name
    class Admin:
        pass

class Location(models.Model):
    institution = models.ForeignKey(Institution)
    location_name_se = models.CharField(max_length=255, null=True, blank=True)
    location_name_en = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    ssid = models.CharField(max_length=255)
    enc_level = models.CharField(max_length=255)
    port_restrict = models.BooleanField()
    transp_proxy = models.BooleanField()
    ipv6 = models.BooleanField()
    nat = models.BooleanField()
    ap_no = models.IntegerField()
    wired = models.BooleanField()
    info_url_se = models.URLField(null=True, blank=True)
    info_url_en = models.URLField(null=True, blank=True)
    area = models.TextField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % self.location_name_en
    class Admin:
        pass
