from django.conf.urls import url
from . import views

app_name= 'rate'
urlpatterns=[
    url(r'^check_rate/$',views.check_rate,name='check_rate'),

]
