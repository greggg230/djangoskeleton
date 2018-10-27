from django.conf.urls import url

from djangoskeleton.apps.core.views import IndexView

app_name = 'core'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='main'),
]
