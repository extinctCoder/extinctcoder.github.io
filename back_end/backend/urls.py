from django.conf.urls import include, url
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url('', include('snippets.urls')),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
