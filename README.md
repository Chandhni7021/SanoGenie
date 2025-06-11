# 🧠 SenoGenie

SenoGenie is an AI-powered webpage that predicts diseases based on user-input symptoms and provides personalized dietary recommendations and health descriptions. Built with a trained Random Forest model and a Flask web interface, SenoGenie bridges AI and healthcare to support smarter, faster, and more accessible health insights.

🌟 Key Features

- ✅ Disease Prediction: Predicts probable diseases based on selected symptoms  
- 🍽️ Dietary Recommendations: Provides nutrition suggestions tailored to the predicted condition   
- 🧠 Trained AI Model: Uses a Random Forest Classifier trained on symptom-disease data  
- 🖥️ Interactive Web UI: Built using Flask for a simple, intuitive user experience

🖼️ Demo Preview
![IMG-20250611-WA0052](https://github.com/user-attachments/assets/16a21f7d-9868-4943-9285-8e734048bfd2)
![IMG-20250611-WA0051](https://github.com/user-attachments/assets/9b30bece-5a24-4112-a361-c80bfa157bc6)
![IMG-20250611-WA0053](https://github.com/user-attachments/assets/f5f802e6-3c4a-469b-9c78-88ed48f8a6f8)

📊 Dataset Details

- Training.csv: Contains binary-encoded symptoms and target diseases  
- description.csv: Maps diseases to brief explanations  
- diets.csv: Maps diseases to ideal diet/nutrition plans

🧪 How It Works

1. Users select symptoms from a checklist.
2. Symptoms are converted into a binary input vector.
3. The trained Random Forest model predicts the most probable disease.
4. The app displays the disease name, a short description, and dietary recommendations.

⚙️ Tech Stack

- Language: Python  
- Framework: Flask  
- ML Library: scikit-learn (Random Forest Classifier)  
- Data Handling: pandas  
- Web: HTML (Jinja2 templates), Flask routing

🚀 Getting Started

✅ Prerequisites

Make sure you have Python 3.x installed. Then:

📁 Files Explained

train_model.py: Trains the Random Forest model and saves model.pkl

app.py: Main Flask application serving the interface and prediction logic

model.pkl: Pre-trained model used for prediction

description.csv: Contains disease info to be displayed

diets.csv: Contains disease-wise diet suggestions

index.html: User symptom input page

result.html: Prediction result page

🔒 Disclaimer
This app is meant for educational and informational purposes only and should not be considered medical advice. For real health concerns, consult a licensed physician.

📜 License
This project is open-source and free to use under the MIT License.


