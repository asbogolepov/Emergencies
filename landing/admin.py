from django.contrib import admin
from landing.models import *

class SubscriberAdmin (admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ('name',)
    search_fields = ["name", "email"]
    # exclude = ["name"]
    # fields = ["email"]



    class Meta:
        model = Subscriber
admin.site.register(Subscriber, SubscriberAdmin)