import pandas as pd
import os

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

merged_data = pd.read_csv("data/merged_data.csv")

X = merged_data[['qualifying_position', 'previous_podiums', 'constructor_performance', 'track_type']]  # Your feature columns
y = merged_data['race_winner']  # Target column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
