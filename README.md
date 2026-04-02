VoltGuard Pro: Community Fault System ⚡

VoltGuard Pro is a sophisticated sociotechnical platform developed for the NHCI63110 assignment. It bridges the communication gap between community members and municipal infrastructure teams by providing real-time, geospatial tracking of electrical and utility faults.
🚀 Project Overview

In many communities, infrastructure reporting is a "black hole"—users report issues but never receive feedback. VoltGuard Pro solves this by using a Bento Box UI that provides immediate visual confirmation of fault status (Pending, In Progress, Resolved) through an interactive Google Maps interface.
Core Features

    Live Geospatial Dashboard: Real-time mapping of faults using the Google Maps API.

    Smart Reporting: A mobile-responsive form with Auto-GPS detection for high-accuracy location logging.

    Operations Center: A secure, administrative portal for technicians to manage the incident queue and dispatch crews.

    Status Synchronization: Automated color-coding (Red/Blue/Green) that updates across the user and admin portals simultaneously.

🛠️ Tech Stack

    Backend: Python / Django (MVT Architecture)

    Frontend: Tailwind CSS (Glassmorphism design), JavaScript

    Database: SQLite (Development) / PostgreSQL (Production ready)

    APIs: Google Maps JavaScript API, Geolocation API

    Design: Human-Computer Interaction (HCI) principles, Responsive Grid Layout

📸 System Screenshots
Live Community Dashboard	Smart Reporting Form	Operations Management
		
(Note: Please replace these with your actual screenshot files in your repository)		
⚙️ Installation & Setup

    Clone the repository:
    Bash

    git clone [Your GitHub Link Here]
    cd community_fault_system

    Create a Virtual Environment:
    Bash

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    Install Dependencies:
    Bash

    pip install -r requirements.txt

    Run Migrations:
    Bash

    python manage.py migrate

    Start the Server:
    Bash

    python manage.py runserver

    Access the app at http://127.0.0.1:8000/

🧪 Iterative Design & AI Evaluation

This project followed a rigorous Iterative Design Process. Initial wireframes were critiqued by AI tools to identify usability bottlenecks.

    Improvement: Based on AI feedback, a Success Modal was added to provide users with a Reference ID, improving the "Visibility of System Status."

    Improvement: The "Smart Location" feature was implemented to reduce manual data entry errors for mobile users.

👨‍💻 Developer Information

    Name: Richard Ramashala

    Student Number: 202306214

    Module: NHCI63110 - Human-Computer Interaction

    Institution: [Your Institution Name]

📄 License

This project is for academic purposes as part of the NHCI63110 curriculum.
