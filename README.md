# 🚑 Healthify+ – Smart Healthcare Companion App

**Healthify+** is a smart health companion web application designed to enhance emergency responsiveness, simplify medical service access, and educate users on critical first aid — now enhanced with insurance integration support.

---

## 🌟 Key Features

- 🤖 **AI-Powered Symptom Analysis**  
  Uses AI to analyze user-reported symptoms and provide early triage insights.

- 🧭 **Location-Based Hospital Referrals**  
  Finds nearby hospitals or clinics in real time using `hospitals_hyderabad.csv` and Google Maps integration.

- 🧠 **CPR & First Aid Modules**  
  Learn life-saving techniques through interactive guides.

- 📷 **Image-Based First Aid Support**  
  Upload injury images and receive first aid suggestions using image analysis (future feature).

- 🧑‍⚕️ **Doctor Consultation**  
  Book secure 1-on-1 online consultations with verified doctors.

- 🛡 **Health Insurance Integration**  
  - Search & compare plans  
  - Link existing policies  
  - Get symptom-based coverage suggestions  
  - Check hospital eligibility

---

## 🛠 Tech Stack

| Layer         | Technologies                                  |
|---------------|-----------------------------------------------|
| Frontend      | HTML, CSS, Bootstrap                          |
| Backend       | Python (Flask), JavaScript                    |
| Templates     | Jinja2-based HTML templates                   |
| Data Storage  | CSV (Hospitals), PDFs                         |
| AI Modules    | ChatGPT API (TechStack), planned MedBERT      |
| APIs          | Google Maps                                   |

---

## 📁 Project Structure

```bash
HealthifyPlus/
├── certificates/                   # (Optional) certificate storage
├── Code/                           # Python scripts and compiled files
│   ├── __pycache__/
│   │   └── data.cpython-311.pyc
│   └── data.py                     # Data handling & logic
│
├── static/                         # Static assets
│   ├── logo-removebg-preview.png
│   ├── logo.jpeg
│   └── style.css
│
├── templates/                      # HTML Templates (Jinja2)
│   ├── about.html
│   ├── base.html
│   ├── certificate_template.html
│   ├── Courses.html
│   ├── DoctorConsultation.html
│   ├── FirstAidGuide.html
│   ├── HealthInsurance.html
│   ├── home.html
│   ├── Hospitals.html
│   ├── login.html
│   ├── register.html
│   ├── SymptomChecker.html
│   ├── test.html
│
├── data/                           # Contains external datasets
│   └── hospitals_hyderabad.csv
│
├── .env                            # Environment variables
├── Base_Papers_Healthify.pdf       # Research/Reference Docs
├── Healthify.pdf                   # Documentation
├── Healthify+.docx                 # App Concept/Report
├── Healthify+.pdf                  # Final App Report/Presentation
├── LICENSE
└── README.md                       # You’re here!
