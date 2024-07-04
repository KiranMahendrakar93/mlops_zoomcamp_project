import requests

details = {
    'StudentID': 1001,
    'Age': 17,
    'Gender': 1,
    'Ethnicity': 0,
    'ParentalEducation': 2,
    'StudyTimeWeekly': 1.7803355189521382,
    'Absences': -0.8908223715622926,
    'Tutoring': 1,
    'ParentalSupport': 2,
    'Extracurricular': 0,
    'Sports': 0,
    'Music': 1,
    'Volunteering': 0,
    'GPA': 2.929195591667681,
    }

response = requests.post(url="http://127.0.0.1:5000/api", json=details)
print(response.text)