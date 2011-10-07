from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def saml_login(request):
    if request.user.is_authenticated():
        update = False
        for attrib_name, meta_name in (("first_name", "HTTP_GIVENNAME"),
                                       ("last_name", "HTTP_SN"),
                                       ("email", "HTTP_MAIL")):
            attrib_value = getattr(request.user, attrib_name)
            meta_value = request.META.get(meta_name)
            if meta_value and not attrib_value or attrib_value == "(null)":
                setattr(request.user, attrib_name, meta_value)
                update = True
        if request.user.password == "":
            request.user.password = "(not used for federated logins)"
            update = True
        if update:
            request.user.save()
        next = request.GET['next']
        if next is not None:
            return HttpResponseRedirect(next)
    else:
        pass
    return HttpResponseRedirect("/")

def saml_logout(request):
    logout(request)
    return HttpResponseRedirect("/Shibboleth.sso/Logout")
