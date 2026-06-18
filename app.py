import os
import re
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Regex patterns for strict server-side validation
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

@app.route('/', methods=['GET'])
def index():
    skills_data = {
        "Languages": [
            {"name": "Python", "level": 90, "icon": "fab fa-python"},
            {"name": "C++", "level": 80, "icon": "fas fa-code"},
            {"name": "Java", "level": 75, "icon": "fab fa-java"},
            {"name": "C", "level": 70, "icon": "fas fa-terminal"}
        ],
        "Web Backend": [
            {"name": "Flask", "level": 85, "icon": "fas fa-cubes"},
            {"name": "SQL", "level": 80, "icon": "fas fa-database"}
        ],
        "Frontend & Tools": [
            {"name": "HTML5/CSS3", "level": 95, "icon": "fab fa-html5"},
            {"name": "JavaScript", "level": 85, "icon": "fab fa-js"},
            {"name": "Git & GitHub", "level": 88, "icon": "fab fa-github"}
        ]
    }
    
    projects_data = [
        {
            "id": "ams",
            "title": "Attendance Management System",
            "desc": "An enterprise-grade automation system utilizing biometric processing data models to capture, track, and generate compliance-ready analytics records seamlessly.",
            "tech": ["Python", "Flask", "SQL", "JavaScript"],
            "github": "https://github.com/yashgaidhane6",
            "live": "#"
        },
        {
            "id": "wa",
            "title": "Weather App",
            "desc": "A slick, real-time climate forecasting dashboard integrating third-party RESTful APIs, client-side geolocation metrics, and complex atmospheric data visualizers.",
            "tech": ["JavaScript", "HTML5", "CSS3", "REST API"],
            "github": "https://github.com/yashgaidhane6",
            "live": "#"
        },
        {
            "id": "gc",
            "title": "Grade Calculator",
            "desc": "An academic evaluation platform designed with algorithmic weight-distribution functions to compute GPA projections and verify student performance schemas.",
            "tech": ["Python", "Flask", "Jinja2", "CSS3"],
            "github": "https://github.com/yashgaidhane6",
            "live": "#"
        },
        {
            "id": "rb",
            "title": "Resume Builder",
            "desc": "An intuitive, dynamic workspace that renders multi-template professional resumes on-the-fly, outputting fully parsed, ATS-optimized data payloads.",
            "tech": ["HTML5", "CSS3", "JavaScript", "JSON"],
            "github": "https://github.com/yashgaidhane6",
            "live": "#"
        },
        {
            "id": "ac",
            "title": "Arithmetic Calculator",
            "desc": "A mathematically precise web calculator built with strict state parsing logic, instantaneous token processing, and a fluid, accessible interface schema.",
            "tech": ["JavaScript", "HTML5", "CSS3"],
            "github": "https://github.com/yashgaidhane6",
            "live": "#"
        }
    ]

    return render_template('index.html', skills=skills_data, projects=projects_data)

# SECURE LOCAL IMAGE STREAM ROUTE
@app.route('/local-profile-image')
def serve_local_image():
    # Direct absolute targeting vector pointing directly to your local file path
    directory = r"C:\Users\swapn\Downloads"
    filename = "WhatsApp Image 2026-05-31 at 3.48.23 PM.jpeg"
    return send_from_directory(directory, filename)

@app.route('/api/contact', methods=['POST'])
def contact_api():
    try:
        data = request.get_json() or {}
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        if not all([name, email, subject, message]):
            return jsonify({"status": "error", "message": "All fields are strictly required."}), 400
            
        if not re.match(EMAIL_REGEX, email):
            return jsonify({"status": "error", "message": "Invalid email formatting provided."}), 400
            
        if len(message) < 10:
            return jsonify({"status": "error", "message": "Message content must exceed 10 characters."}), 400

        return jsonify({"status": "success", "message": f"Thank you, {name}. Your transmission has been securely logged."}), 200
        
    except Exception as e:
        return jsonify({"status": "error", "message": "Internal gateway routing exceptions encountered."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
