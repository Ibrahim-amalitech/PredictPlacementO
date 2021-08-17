from django.contrib import admin
from django.db import models



from .models import  Placement
#Make fields which are hidden in forms(editable=False) appear in admin
class PlacementAdmin(admin.ModelAdmin):
    def get_readonly_fields(self,request,obj=None):
        return [f.name for f in obj._meta.fields if not f.editable]
# Register your models below:
admin.site.register(Placement,PlacementAdmin)

