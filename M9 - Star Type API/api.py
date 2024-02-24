from fastapi import FastAPI
from star_data import StarProperties, StarTypePrediction
from predictor import load_model, make_predictions
import numpy as np

app = FastAPI()

model = load_model('model.pkl')

@app.get('/')
def index_route():
    return {"Health" : "Ok"}

@app.post('/predict', response_model=StarTypePrediction)
def prediction(sp: StarProperties):
    input_features = [[sp.temperature, sp.luminosity, sp.radius, sp.abs_mag]]
    predicted_class, probs, classes = make_predictions(model, input_features)
    return {
        'predicted_probabilities' : dict(zip(classes, probs)),
        'predicted_class' : predicted_class,
        'confidence_score' : str(round(np.max(probs),3)*100) + '%'
    }

'''
Test on Real Star Data Taken from Wikipedia:- 
Betelgeuse (Supergiant) ~ https://en.wikipedia.org/wiki/Betelgeuse
Beta Pictoris (Main Seq) ~ https://en.wikipedia.org/wiki/Beta_Pictoris
Sirus (White Dwarf) ~ https://en.wikipedia.org/wiki/Sirius
'''
