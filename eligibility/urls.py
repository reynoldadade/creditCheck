from django.conf.urls import url
from . import views


app_name = 'eligibility'
urlpatterns = [
    #  /eligibility/
    url(r'^$', views.index, name='index'),
    url(r'^check_eligibility/$',views.check_eligibility,name='check_eligibility')

]
