"""
drf_demo URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from polls.views import QuestionViewSet


router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)


API_TITLE = 'Polls API'
API_DESCRIPTION = 'A demo of the Django Tutorial implementing DRF'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
