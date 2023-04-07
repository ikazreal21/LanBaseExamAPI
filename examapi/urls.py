from django.urls import path
from .views import *
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


urlpatterns = [
    path('upload/', UploadViewSet.as_view(), name='upload'),
    path('questionlist/', QuestionList.as_view(), name='upload'),
    path('apidocs/', get_schema_view(
        title="LAN BASE EXAM SYSTEM",
        description="API for a LAN base exam system"
    ),  name='apidocs-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'apidocs-schema'}
    ), name='swagger-ui'),
]