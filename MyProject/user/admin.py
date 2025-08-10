from django.contrib import admin
from.models import *


# Register your models here.

class contactusAdmin(admin.ModelAdmin):
    list_display=("name","mobile","email","massage")

admin.site.register(contactus,contactusAdmin)

class igalleryAdmin(admin.ModelAdmin):
    list_display=("picture","title")

admin.site.register(igallery,igalleryAdmin)

class ourplacementAdmin(admin.ModelAdmin):
    list_display=("name","picture","psession","company","branch")

admin.site.register(ourplacement,ourplacementAdmin)

class mycourseAdmin(admin.ModelAdmin):
    list_display=("branch","picture","seats")

admin.site.register(mycourse,mycourseAdmin)

class ourfaucltyAdmin(admin.ModelAdmin):
    list_display=("name","picture","qualification","experience","fposts")

admin.site.register(ourfaculty,ourfaucltyAdmin)

class myfacilitiesAdmin(admin.ModelAdmin):
    list_display=("name","picture")

admin.site.register(myfacilities,myfacilitiesAdmin)

class noticeAdmin(admin.ModelAdmin):
    list_display=("id","name")

admin.site.register(notice,noticeAdmin)