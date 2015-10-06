from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from outside_listing import views
from django.contrib import admin


urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^map/$', views.map, name="map"),
                       url(r'^lead/(?P<id>[0-9]+)/$', views.lead_detail, name="lead-detail"),
                       url(r'^lead/(?P<id>[0-9]+)/closed/$', login_required(views.LeadClosedView.as_view()), name="lead-closed"),
                       url(r'^lead/(?P<id>[0-9]+)/repeat/$', login_required(views.LeadRepeatView.as_view()), name="lead-repeat"),
                       url(r'^lead/(?P<id>[0-9]+)/feedback/$', login_required(views.LeadFeedbackView.as_view()), name="lead-feedback"),
                       url(r'^admin/', include(admin.site.urls)),

                       )
