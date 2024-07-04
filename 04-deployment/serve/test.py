import requests

# details = {
#     'StudentID': 1001,
#     'Age': 17,
#     'Gender': 1,
#     'Ethnicity': 0,
#     'ParentalEducation': 2,
#     'StudyTimeWeekly': 1.7803355189521382,
#     'Absences': -0.8908223715622926,
#     'Tutoring': 1,
#     'ParentalSupport': 2,
#     'Extracurricular': 0,
#     'Sports': 0,
#     'Music': 1,
#     'Volunteering': 0,
#     'GPA': 2.929195591667681,
#     }

details = {'StudentID': 1011,
  'Age': 17,
  'Gender': 0,
  'Ethnicity': 0,
  'ParentalEducation': 1,
  'StudyTimeWeekly': 0.3679266916912635,
  'Absences': -0.41832453625501304,
  'Tutoring': 0,
  'ParentalSupport': 1,
  'Extracurricular': 0,
  'Sports': 0,
  'Music': 0,
  'Volunteering': 0,
  'GPA': 2.1471716250185144,
  'GradeClass': 3.0}

response = requests.post(url="http://127.0.0.1:5000/api", json=details)
print(response.text)