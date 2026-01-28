from django.contrib import admin
from . models import *

registry = [Sermon,VisitationAudit,VisitUsInfo,Preacher,Staff,Records,ScriptureReference]

admin.site.register(registry)