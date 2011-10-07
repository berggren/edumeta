from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=255)
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
    info_url_en = models.URLField()
    info_url_sv = models.URLField()
    timecreated = models.DateTimeField(auto_now_add=True)
    lastupdated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % self.location_name
    class Admin:
        pass

class Institution(models.Model):
    realm = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    type = models.IntegerField()
    org_name_sv = models.CharField(max_length=255)
    org_name_en = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    info_url_sv = models.URLField()
    info_url_en = models.URLField()
    policy_url_sv = models.URLField()
    policy_url_en = models.URLField()
    location = models.ManyToManyField(Location)
    timecreated = models.DateTimeField(auto_now_add=True)
    lastupdated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % self.org_name_sv
    class Admin:
        pass
