# Pydantic Imports
from pydantic import BaseModel, Field

class StarProperties(BaseModel):
    """Model representing properties of a star.

    Attributes:
        temperature (int): Temperature of the star in Kelvin.
        luminosity (float): Luminosity of the star with respect to the Sun.
        radius (float): Radius of the star in solar radii.
        abs_mag (float): Absolute magnitude of the star.
    """
    temperature: int = Field(description="Temperature of the star in Kelvin", example=2376)
    luminosity: float = Field(description="Luminosity of the star wrt Sun", example=0.00073)
    radius: float = Field(description="Radius of the star in solar radii", example=0.127)
    abs_mag: float = Field(description="Absolute magnitude of the star", example=17.22)

# Example to be used in StarTypePrediction's predicted_probabilities
pred_prob_example = {
    "Brown Dwarf": 0.6588668588268463,
    "Hypergiant": 0.0010894578637846593,
    "Main Sequence": 0.005465854764863855,
    "Red Dwarf": 0.26195464795013196,
    "Supergiant": 0.0010449570211609447,
    "White Dwarf": 0.07157822357321225
  }

class StarTypePrediction(BaseModel):
    """Model representing the prediction results for a star's type.

    Attributes:
        predicted_probabilities (dict): Predicted probabilities for all classes.
        predicted_class (str): Predicted class based on the highest probability.
        confidence_score (str): Confidence score indicating the model's certainty in the predicted class.
    """
    predicted_probabilities: dict = Field(description="Predicted probabilities for all classes.", example=pred_prob_example)
    predicted_class: str = Field(description="Predicted class based on the highest probability.", example='Brown Dwarf')
    confidence_score: str = Field(description="Confidence score indicating the model's certainty in the predicted class.", example="65.9%")