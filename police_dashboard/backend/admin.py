from django.contrib import admin
from .models import Officer, Login, Patrol,Report,FIR,FIRStatus

admin.site.register(Officer)
admin.site.register(Login)
admin.site.register(Patrol)
admin.site.register(Report)
admin.site.register(FIR)
admin.site.register(FIRStatus)