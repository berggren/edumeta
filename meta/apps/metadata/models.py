from django.db import models

class Institution(models.Model):
    realm = models.CharField(max_length=255)
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
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % self.org_name_sv
    def get_locations(self):
        return Location.objects.filter(institution=self)
    def get_contacts(self):
        return Contact.objects.filter(institution=self)
    class Admin:
        pass

class Contact(models.Model):
    institution = models.ForeignKey(Institution)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s - %s' % (self.institution, self.name)
    class Admin:
        pass

class Location(models.Model):
    institution = models.ForeignKey(Institution)
    location_name = models.CharField(max_length=255)
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
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % self.location_name
    class Admin:
        pass
