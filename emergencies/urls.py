from django.conf.urls import url, include
from emergencies import views


urlpatterns = [
    url(r'^$', views.emergencies, name='emergencies'),
    # url(r'^emergency/(?P<emergency_id>/w+)$', views.emergency, name='emergency'),
]

