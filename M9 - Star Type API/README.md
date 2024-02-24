# 🌟 Star Type Prediction API 🌠

🔸 Welcome to the Star Type Prediction API!<br>
🔸 This project deploys a Logistic Regression model as an API using FastAPI.

## ⚙️ Setup
Follow these steps to set up the project on your local machine:
1. **Clone the Repository:**
```
git clone https://github.com/SpartificialUdemy/PSA.git
cd "M9 - Star Type API"
```
2. **Create a Virtual Environment and Activate it:** 
```
python -m venv venv-name
.\venv-name\Scripts\activate
```
3. **Install Dependencies:**
```
pip install -r requirements.txt
```

## 💻 Running the App
1. **Run the FastAPI App:**
```
uvicorn api:app --host YOUR_IP --port YOUR_PORT --reload
```
Replace `YOUR_IP` and `YOUR_PORT` with the desired IP address and port number.

2. **Access Swagger UI:**<br>
🔸 Open your web browser and navigate to `http://YOUR_IP:YOUR_PORT/docs` to access the Swagger UI.<br>
🔸 Here, you can interact with the API, input star properties, and receive predictions.

## ✨ Example of Request and Response bodies via Swagger UI

🔸 **Request body:-**
```
{
  "temperature": 2376,
  "luminosity": 0.00073,
  "radius": 0.127,
  "abs_mag": 17.22
}
```

🔸 **Response body:-**
```
{
  "predicted_probabilities": {
    "Brown Dwarf": 0.6588668588268786,
    "Hypergiant": 0.001089457863784464,
    "Main Sequence": 0.005465854764863331,
    "Red Dwarf": 0.26195464795010903,
    "Supergiant": 0.0010449570211607344,
    "White Dwarf": 0.07157822357320391
  },
  "predicted_class": "Brown Dwarf",
  "confidence": "65.9%"
}
```

## 💫 Test the API on Real Star Data taken from Wikipedia                 
🔸[Betelgeuse (Supergiant)](https://en.wikipedia.org/wiki/Betelgeuse)              
🔸[Beta Pictoris (Main Seq)](https://en.wikipedia.org/wiki/Beta_Pictoris)             
🔸[Sirus A (Main Seq)](https://en.wikipedia.org/wiki/Sirius)                  

## 📁 Project Structure
🔸 **api.py:** FastAPI application defining the API endpoints.<br>
🔸 **ml_star_type_prediction.ipynb:** Jupyter Notebook used for training the model and saving it as model.pkl.<br>
🔸 **model.pkl:** Serialized trained model for star type prediction.<br>
🔸 **predictor.py:** Module containing functions to load the model and make predictions.<br>
🔸 **requirements.txt:** List of Python dependencies for the project.<br>
🔸 **star_data.py:** Pydantic BaseModel and Field definitions along with set examples.<br>
🔸 **star_type_.csv:** Dataset used for training the model.<br>

## 🤝 Contribute/Queries/Suggestions
🔸 Feel free to explore and contribute to this project.<br>
🔸 If you find this project helpful, consider giving it a star! **(A star for a Star Type Predictor?)** ⭐️<br>

**Happy Star Type Prediction!** 🌌
