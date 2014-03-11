from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pari.faces.views import FaceList, FaceDetail, FaceImageDetail

urlpatterns = patterns('pari.faces.views',
                       url(r'^(?P<alphabet>\w)/', FaceDetail.as_view(template_name="faces/face_detail.html"), name='face-detail'),
                       url(r'^$', FaceList.as_view(), name='face-list'),
                       )

urlpatterns += staticfiles_urlpatterns()