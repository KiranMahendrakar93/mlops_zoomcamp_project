# import requests
import predict

data = {
    'StudentID': 1001.0, 
    'Age': 17.0, 
    'Gender': 1.0, 
    'Ethnicity': 0.0, 
    'ParentalEducation': 2.0, 
    'StudyTimeWeekly': 19.833722807854716, 
    'Absences': 7.0, 
    'Tutoring': 1.0, 
    'ParentalSupport': 2.0, 
    'Extracurricular': 0.0, 
    'Sports': 0.0, 
    'Music': 1.0, 
    'Volunteering': 0.0, 
    'GPA': 2.929195591667681, 
}

# url = 'http://localhost:9696/predict'
# response = requests.post(url, json=data)
# print(response.json())

features = predict.prepare_features(data)
pred = predict.predict(features)
print(pred)