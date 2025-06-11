import os
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 🔥 Always get the current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ Clean path to your dataset
data_path = os.path.join(BASE_DIR, "data", "Training.csv")
df = pd.read_csv(data_path)

# 🧠 Assume last column is the target
X = df.iloc[:, :-1]  # All columns except last
y = df.iloc[:, -1]   # Last column as target

# 🧪 Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🌳 Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 📦 Save model to model.pkl
model_path = os.path.join(BASE_DIR, "model.pkl")
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to:", model_path)
