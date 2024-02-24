# Standard Imports
from fastapi import FastAPI
import numpy as np

# Local Imports
from star_data import StarProperties, StarTypePrediction
from predictor import load_model, make_predictions

# Creating a FastAPI app instance and loading a machine learning model from MODEL_PATH
app = FastAPI()
MODEL_PATH = 'model.pkl'
model = load_model(MODEL_PATH)

@app.get('/')
def index_route():
    """Health Check Endpoint
    
    Returns:
        dict: A dictionary indicating the health status of the application.
    """
    return {"Health" : "Ok"}

@app.post('/predict', response_model=StarTypePrediction)
def prediction(sp: StarProperties):
    """Endpoint for predicting the star type based on given star properties.

    Parameters:
        sp (StarProperties): The star properties including temperature, luminosity, radius, and absolute magnitude.

    Returns:
        dict: A dictionary containing the predicted probabilities for each star type,
              the predicted star class, and the confidence score.
    """
    input_features = [[sp.temperature, sp.luminosity, sp.radius, sp.abs_mag]]
    predicted_class, probs, classes = make_predictions(model, input_features)
    pred_probs = dict(zip(classes, probs))
    sorted_pred_probs = dict(sorted(pred_probs.items(), key = lambda item: item[1], reverse=True))
    return {
        'predicted_probabilities' : sorted_pred_probs,
        'predicted_class' : predicted_class,
        'confidence_score' : str(round(np.max(probs),3)*100) + '%'
    }