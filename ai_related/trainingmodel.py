import json
import numpy as np
import joblib
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# -------- Training Data (Example) --------
training_data = [{"tag": "input", "id": "userName", "name": "username", "type": "text", "text": None}, 
{"tag": "input", "id": "password", "name": "password", "type": "password", "text": None}, 
{"tag": "button", "id": None, "name": None, "type": "submit", "text": "Login"}]


labels = ["usernameInput", "passwordInput", "submitButton"]

# Replace None with empty strings
for item in training_data:
    for key in item:
        if item[key] is None:
            item[key] = ""

X = training_data
y = labels

# Vectorize features and encode labels
vectorizer = DictVectorizer(sparse=False)
X_vectorized = vectorizer.fit_transform(X)

le_target = LabelEncoder()
y_encoded = le_target.fit_transform(y)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y_encoded, test_size=0.33, random_state=42)
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Save model and preprocessors
joblib.dump(clf, "Bikram/model.pkl")
joblib.dump(vectorizer, "Bikram/vectorizer.pkl")
joblib.dump(le_target, "Bikram/label_encoder.pkl")

# Evaluate
y_pred = clf.predict(X_test)
unique_labels = np.unique(np.concatenate([y_test, y_pred]))
unique_target_names = le_target.inverse_transform(unique_labels)

print(classification_report(y_test, y_pred, labels=unique_labels, target_names=unique_target_names))
print("✅ Model saved in Bikram folder.")
