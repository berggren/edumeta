from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=255, null=True, blank=True)
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    ssid = models.CharField(max_length=255, null=True, blank=True)
    enc_level = models.CharField(max_length=255, null=True, blank=True)
    port_restrict = models.BooleanField()
    transp_proxy = models.BooleanField()
    ipv6 = models.BooleanField()
    nat = models.BooleanField()
    ap_no = models.IntegerField(null=True, blank=True)
    wired = models.BooleanField()
    info_url_en = models.URLField(null=True, blank=True)
    info_url_sv = models.URLField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % self.location_name
    class Admin:
        pass

class Institution(models.Model):
    realm = models.CharField(max_length=255, null=True, blank=True)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField(null=True, blank=True),
    contact_phone = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    org_name_sv = models.CharField(max_length=255, null=True, blank=True)
    org_name_en = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    info_url_sv = models.URLField(null=True, blank=True)
    info_url_en = models.URLField(null=True, blank=True)
    policy_url_sv = models.URLField(null=True, blank=True)
    policy_url_en = models.URLField(null=True, blank=True)
    location = models.ManyToManyField(Location)
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % self.org_name_sv
    class Admin:
        pass
