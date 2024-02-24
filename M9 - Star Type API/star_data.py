from pydantic import BaseModel, Field

class StarProperties(BaseModel):
    temperature: int = Field(description="Temperature of the star in Kelvin", example=2376)
    luminosity: float = Field(description="Luminosity of the star wrt Sun", example=0.00073)
    radius: float = Field(description="Radius of the star in solar radii", example=0.127)
    abs_mag: float = Field(description="Absolute magnitude of the star", example=17.22)

pred_prob_example = {
    "Brown Dwarf": 0.6588668588268463,
    "Hypergiant": 0.0010894578637846593,
    "Main Sequence": 0.005465854764863855,
    "Red Dwarf": 0.26195464795013196,
    "Supergiant": 0.0010449570211609447,
    "White Dwarf": 0.07157822357321225
  }

class StarTypePrediction(BaseModel):
    predicted_probabilities: dict = Field(description="Predicted probabilities for all classes.", example=pred_prob_example)
    predicted_class: str = Field(description="Predicted class based on the highest probability.", example='Brown Dwarf')
    confidence_score: str = Field(description="Confidence score indicating the model's certainty in the predicted class.", example="65.9%")