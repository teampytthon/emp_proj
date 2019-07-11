from django.conf.urls import url
from . import views

app_name='department'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^department/add/$', views.saveData.as_view(), name='saves'),
    url(r'department/(?P<pk>[0-9]+)/$', views.EditData.as_view(), name='edit'),
    url(r'department/(?P<pk>[0-9]+)/delete/$', views.deleteData.as_view(), name='deletes'),
]

