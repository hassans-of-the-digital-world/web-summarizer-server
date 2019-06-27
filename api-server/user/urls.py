from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

urlpatterns = [
    url('detail/', views.user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
