from django.urls.conf import path
from .views import HomePage
app_name='feed'
urlpatterns=[
    path('',HomePage.as_view(),name='home')
]