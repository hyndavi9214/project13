from app.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('suri/',suri,name='suri'),
]