from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_generic as views

urlpatterns = [
    path('', views.SnippetList.as_view(), name="snippet_list"),
    path('<int:pk>/', views.SnippetDetail.as_view(), name="snippet_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
