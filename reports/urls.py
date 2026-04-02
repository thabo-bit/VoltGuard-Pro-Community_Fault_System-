from django.urls import path
from . import views

urlpatterns = [
    # Main page to show the report form
    path('', views.report_fault, name='report_page'),

    # Success page after submission
    path('submit/', views.report_success, name='report_submit'),
]