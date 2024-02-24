import pickle
import warnings
warnings.filterwarnings('ignore')

def load_model(model_path):
    """
    Load a pre-trained model from a pickle file.

    Parameters:
    - model_path (str): The path to the pickle file containing the pre-trained model.

    Returns:
    - object: The loaded pre-trained model.
    """
    with open(model_path, 'rb') as f:
        return pickle.load(f)    

def make_predictions(model, input_features):
    """
    Make predictions using a loaded model and input features.

    Parameters:
    - model (object): The pre-trained model.
    - input_features (List[List[float]]): Input features for making predictions.

    Returns:
    - Tuple[str, List[float], List[str]]: A tuple containing the predicted class, probabilities, and classes.
    """
    predict_class = model.predict(input_features)[0]
    probabilities = model.predict_proba(input_features)[0]
    classes = model.classes_
    return predict_class, probabilities, classes

