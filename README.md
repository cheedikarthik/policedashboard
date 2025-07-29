# 🚓 Police Dashboard Web App

A web-based application that allows the public to **file FIRs**, **track case status**, access **emergency helpline numbers**, and **view active police unit locations** in real time. Designed to improve transparency and accessibility between citizens and law enforcement.

---

## 📁 Project Structure

police_dashboard/
├── backend/ # Django app
│ ├── init.py
│ ├── admin.py # Admin interface configuration
│ ├── apps.py # App configuration
│ ├── models.py # Database models
│ ├── urls.py # URL routing
│ ├── views.py # API endpoints / views
│ └── pycache/ # Compiled Python files
├── migrations/ # Database migration history
│ ├── 0001_initial.py
│ ├── 0002_officer_patrol_location.py
│ ├── init.py
│ └── pycache/



 Features

- File First Information Reports (FIRs) online.
- Track case progress/status by FIR ID.
- Access emergency helpline contacts.
- View real-time patrol or police unit locations.
- Role-based access for officers and citizens.

 Technologies Used

- **Backend:** Python, Django
- **Database:** PostgreSQL or SQLite (default)
- **Frontend:** (To be added if applicable: React, HTML/CSS, Bootstrap, etc.)
- **Map Integration:** (Optional: Google Maps API / Leaflet.js for location tracking)

 Models Overview (sample)
 
class FIR(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)


 Future Enhancements
 
- Admin dashboard for internal police use

- SMS/email notifications on FIR updates

- Public feedback & rating system for transparency

- Interactive map view with patrol units


