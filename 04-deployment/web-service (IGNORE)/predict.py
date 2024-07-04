import pickle
import pandas as pd

from flask import Flask, request, jsonify

# load misc pkl data
with open(f'/workspaces/mlops_zoomcamp_project/dumps/misc/numeric_features.pkl', 'rb') as f_in:
    numeric_features = pickle.load(f_in)

with open(f'/workspaces/mlops_zoomcamp_project/dumps/misc/categoric_features.pkl', 'rb') as f_in:
    categoric_features = pickle.load(f_in)

# load model
with open(f'/workspaces/mlops_zoomcamp_project/dumps/models/Support_Vector_Machine_model.pkl', 'rb') as f_in:
    model = pickle.load(f_in)


def prepare_features(df):

    if isinstance(df, dict):
        df = [df]
    if not isinstance(df, pd.DataFrame):    
        df = pd.DataFrame(df)

    # cleaning
    columns_to_drop = ['GPA', 'StudentID', 'Age', 'GradeClass']
    numeric_columns = [feat for feat in numeric_features if feat not in columns_to_drop]
    categoric_columns = [feat for feat in categoric_features if feat not in columns_to_drop]
    
    df[numeric_columns] = df[numeric_columns].astype('float64')

    
    # transforming
    for column in categoric_columns:  
        with open(f'/workspaces/mlops_zoomcamp_project/dumps/misc/{column}_label_encoder.pkl', 'rb') as f_in:
            encoder = pickle.load(f_in)
            df[column] = encoder.transform(df[column])
    
    for column in numeric_columns:
        with open(f'/workspaces/mlops_zoomcamp_project/dumps/misc/{column}_standard_scaler.pkl', 'rb') as f_in:
            scaler = pickle.load(f_in)
            df[column] = scaler.transform(df[[column]])

    features = df.to_dict(orient='records')
                          
    return features


def predict(features):
    preds = model.predict(features)
    return preds[0]


# app = Flask('mlops_zoomcamp_proj')


# @app.route('/predict', methods=['POST'])
# def predict_endpoint():
#     data = request.get_json()

#     features = prepare_features(data)
#     pred = predict(features)

#     result = {
#         'duration': pred
#     }

#     return jsonify(result)


# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=9696)