from django.conf.urls import url

from djangoskeleton.apps.core.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='main'),
]
