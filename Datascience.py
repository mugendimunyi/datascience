# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score
import pandas as pd

# Sample dataset (replace this with your actual dataset)
data = {
    'Temperature': [50, 60, 70, 80, 90, 55, 75, 85, 95, 100],
    'Pressure': [30, 40, 50, 60, 70, 35, 55, 65, 75, 80],
    'Vibration': [0.1, 0.2, 0.3, 0.4, 0.5, 0.15, 0.25, 0.35, 0.45, 0.55],
    'Oil_Level': [50, 40, 30, 20, 10, 45, 35, 25, 15, 5],
    'Equipment_Status': [1, 1, 0, 1, 0, 1, 0, 1, 1, 0]  # Target variable (0: Failure, 1: Functioning)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define features (X) and target variable (y)
X = df.drop('Equipment_Status', axis=1)
y = df['Equipment_Status']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier
clf = DecisionTreeClassifier(random_state=42)

# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Display the decision tree rules
tree_rules = export_text(clf, feature_names=list(X.columns))
print("Decision Tree Rules:")
print(tree_rules)
