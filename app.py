from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open('model/model.pkl', 'rb'))

desc = pd.read_csv('model/data/description.csv')
diets = pd.read_csv('model/data/diets.csv')
symptoms = pd.read_csv('model/data/Training.csv').columns[:-1]

@app.route('/')
def index():
    return render_template('index.html', symptoms=symptoms)

@app.route('/predict', methods=['POST'])
def predict():
    input_symptoms = request.form.getlist('symptoms')
    input_vector = [1 if s in input_symptoms else 0 for s in symptoms]
    prediction = model.predict([input_vector])[0]

    disease_info = desc.loc[desc["Disease"] == prediction, "Description"].values[0]
    diet_info = diets.loc[diets["Disease"] == prediction, "Diet"].values[0]

    return render_template("result.html", disease=prediction, description=disease_info, diet=diet_info)

if __name__ == '__main__':
    app.run(debug=True)
