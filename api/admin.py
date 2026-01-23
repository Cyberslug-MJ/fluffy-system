from django.contrib import admin
from . models import *

registry = [Sermon,VisitationAudit,VisitUsInfo,Preacher,Staff]

admin.site.register(registry)