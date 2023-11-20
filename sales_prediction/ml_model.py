import joblib

def load_logistic_regression_model():
    model_path = 'sales_prediction/linear_regression_model.joblib'
    return joblib.load(model_path)

def predict_sales(tv, newspaper, radio):
    model = load_logistic_regression_model()
    features = [[float(tv), float(newspaper), float(radio)]]
    prediction = model.predict(features)
    return int(prediction[0])