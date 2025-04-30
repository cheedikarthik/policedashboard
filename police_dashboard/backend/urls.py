from django.urls import path
from . import views

urlpatterns = [
    # Define the root path to render the index view
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('loginadmin/', views.loginadmin_view, name='loginadmin'),
    path('indexpublic/', views.indexpublic_view, name='indexpublic'),
    path('reportcrime/', views.reportcrime_view, name='reportcrime'),
    path('submit-crime-report/', views.report_crime_view, name='submit_crime_report'),
    path('filefir/', views.filefir_view, name='filefir'),
    path('firstatus/', views.firstatus_view, name='firstatus'),
    path('helplines/', views.emergency_helpline_view, name='helplines'),
    path('crimereport/', views.crimereport_view, name='crimereport'),
    path('index/', views.index_view, name='indexcop'),
    path('patroldep/', views.patrol_deployment_view, name='patroldep'),
    path('officermgmt/', views.officer_management_view, name='officermgmt'),
    path('add-officer/', views.add_officer_view, name='add_officer'),
    path('edit-officer/', views.edit_officer_view, name='edit_officer'),
    path('view-logs/', views.view_logs_view, name='view_logs'),
    path('officermgmtadmin/', views.police_management_view, name='officermgmtadmin'),
    path('check-fir-status/<str:fir_id>/', views.check_fir_status, name='check_fir_status'),
    path('check-report-status/<str:report_id>/', views.check_report_status, name='check_report_status'),
]


