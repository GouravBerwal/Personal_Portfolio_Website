from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/', views.resume_view, name='resume'),
    path('contact/', views.contact_submit, name='contact_submit'),
]
