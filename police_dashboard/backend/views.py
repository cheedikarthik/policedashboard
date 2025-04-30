from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import JsonResponse
from .models import FIR, Report

def login_view(request):
    return render(request, 'login.html')

def loginadmin_view(request):
    return render(request, 'loginadmin.html')

def indexpublic_view(request):
    return render(request, 'indexpublic.html')

def reportcrime_view(request):
    return render(request, 'reportcrime.html')

def filefir_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        crime_type = request.POST.get('crime_type')
        incident_date = request.POST.get('incident_date')
        location = request.POST.get('location')
        description = request.POST.get('description')
        fir_file = request.FILES.get('fir_file')

        if not (name and contact and crime_type and incident_date and location and description and fir_file):
            messages.error(request, "All fields are required.")
            return redirect('filefir')

        fs = FileSystemStorage()
        file_path = fs.save(f'fir_files/{fir_file.name}', fir_file)

        FIR.objects.create(
            name=name,
            contact=contact,
            crime_type=crime_type,
            incident_date=incident_date,
            location=location,
            description=description,
            file_path=file_path
        )
        messages.success(request, "FIR submitted successfully!")
        return redirect('filefir')

    return render(request, 'filefir.html')

def firstatus_view(request):
    return render(request, 'firstatus.html')

def crimereport_view(request):
    return render(request, 'crimereport.html')

def report_crime_view(request):
    # This view may process a crime report submission.
    return render(request, 'reportcrime.html')

def check_status_view(request):
    return render(request, 'firstatus.html')

def check_fir_status(request, fir_id):
    fir = get_object_or_404(FIR, fir_id=fir_id)
    return JsonResponse({'status': fir.status})

def check_report_status(request, report_id):
    report = get_object_or_404(Report, report_id=report_id)
    return JsonResponse({'status': report.status})

def emergency_helpline_view(request):
    return render(request, 'helplines.html')

def admin_dashboard_view(request):
    return render(request, 'indexadmin.html')

def add_officer_view(request):
    return render(request, 'add_officer.html')

def edit_officer_view(request):
    return render(request, 'edit_officer.html')

def view_logs_view(request):
    return render(request, 'view_logs.html')

def police_management_view(request):
    # Example: rendering a page with a list of police officers
    police_officers = [
        {'police_id': 'P001', 'name': 'Officer John Doe', 'rank': 'Inspector', 'status': 'On Duty'},
        {'police_id': 'P002', 'name': 'Officer Jane Smith', 'rank': 'Sub-Inspector', 'status': 'Off Duty'},
        {'police_id': 'P003', 'name': 'Officer Alan Walker', 'rank': 'Constable', 'status': 'On Patrol'},
        {'police_id': 'P004', 'name': 'Officer Maria Garcia', 'rank': 'Head Constable', 'status': 'On Duty'},
    ]
    return render(request, 'officermgmt.html', {'police_officers': police_officers})

def crime_dashboard_view(request):
    # Example: dashboard view for crime data
    return render(request, 'indexcop.html')

def crime_report_view(request):
    return render(request, 'crimereport.html')

def index_view(request):
    return render(request, 'index.html')

def patrol_deployment_view(request):
    patrol_units = [
        {'unit_name': 'Alpha Squad', 'location': 'Sector 12', 'police_count': 5, 'status': 'On Duty'},
        {'unit_name': 'Bravo Team', 'location': 'Market Street', 'police_count': 3, 'status': 'Patrolling'},
        {'unit_name': 'Charlie Unit', 'location': 'Station Road', 'police_count': 4, 'status': 'Standby'},
    ]
    return render(request, 'patroldep.html', {'patrol_units': patrol_units})

def officer_management_view(request):
    return render(request, 'officermgmt.html')
