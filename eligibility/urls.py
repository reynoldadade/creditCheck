from django.conf.urls import url
from . import views

urlpatterns = [
    #  /eligibility/
    url(r'^$', views.index, name='index'),
    # /eligibility/99999999
    url(r'^(?P<client_id>[1-9]+)/$',views.detail,name='detail'),
]