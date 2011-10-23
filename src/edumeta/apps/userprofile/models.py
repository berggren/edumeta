from django.db import models
from django.contrib.auth.models import User
from edumeta.apps.metadata.models import Institution

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    institution = models.ManyToManyField(Institution, blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % self.user
    class Admin:
        pass

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])