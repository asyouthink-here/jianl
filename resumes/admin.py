from django.contrib import admin
from .models import *


class Basicadimin(admin.ModelAdmin):
    list_display = ('name', 'birth', 'phonenumber')
    date_hierarchy = 'birth'


admin.site.register(Basic, Basicadimin)
admin.site.register(Education)
admin.site.register(Schooltime)
admin.site.register(Workexperience)
admin.site.register(Project)
admin.site.register(Procedules)
admin.site.register(Rewarded)
admin.site.register(Text)
admin.site.register(Jobintansion)

