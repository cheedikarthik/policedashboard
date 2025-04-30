from django.db import models

class FIR(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    crime_type = models.CharField(max_length=50)
    incident_date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    file_path = models.FileField(upload_to='fir_files/')

    def __str__(self):
        return f"{self.name} - {self.crime_type}"


class FIRStatus(models.Model):
    fir = models.OneToOneField(FIR, on_delete=models.CASCADE, related_name='status_record')
    status = models.CharField(max_length=50)

    def __str__(self):
        # Using the related FIR object's primary key as the identifier.
        return f"FIR {self.fir.id} - {self.status}"


class Report(models.Model):
    report_id = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Report {self.report_id} - {self.status}"
class Officer(models.Model):
    officer_id = models.IntegerField(primary_key=True)
    officer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    rank = models.IntegerField()  # If rank is numeric; otherwise use CharField if you require text
    status = models.CharField(max_length=50)
    attendance = models.IntegerField()
    password = models.CharField(max_length=128)  # In a production app, consider storing a hashed version

    def __str__(self):
        return f"{self.officer_id} - {self.officer_name}"

class Login(models.Model):
    # This model is linked to Officer to verify the officer_id and password during login.
    # The officer_id field is stored as a one-to-one relationship with Officer.
    officer = models.OneToOneField(Officer, on_delete=models.CASCADE)
    password = models.CharField(max_length=128)  # This can be compared against Officer.password

    def __str__(self):
        return f"Login for Officer {self.officer.officer_id}"

class Patrol(models.Model):
    unit_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    police_count = models.IntegerField()
    patrol_status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.unit_name} - {self.location} ({self.patrol_status})"