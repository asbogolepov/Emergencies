from django.contrib import admin
from landing.models import *
from emergencies.models import *


class EmergencyImageInline(admin.TabularInline):
    model = EmergencyImage
    extra = 0


class EmergencyAdmin (admin.ModelAdmin):

    list_display = [field.name for field in Emergency._meta.fields]
    inlines = [EmergencyImageInline]

    search_fields = ["name", "email"]

    class Meta:
        model = Emergency
admin.site.register(Emergency, EmergencyAdmin)


class EmergencyImageAdmin (admin.ModelAdmin):

    list_display = [field.name for field in EmergencyImage._meta.fields]

    search_fields = ["name", "email"]

    class Meta:
        model = Emergency
admin.site.register(EmergencyImage, EmergencyImageAdmin)

class StatusAdmin (admin.ModelAdmin):

    list_display = [field.name for field in Status._meta.fields]

    search_fields = ["name", "email"]

    class Meta:
        model = Status
admin.site.register(Status, StatusAdmin)