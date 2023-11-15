# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score
import pandas as pd

# Sample dataset 
data = {
    'Calibration_Verified': [1, 2, 1, 1, 2, 1, 2, 1, 1, 2],
    'Battery_Status': [1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
    'Firmware_Update': [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    'Environmental_Conditions': [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    'Thermometer_Status': [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]  # Target variable (0: Failure, 1: Functioning)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define features (X) and target variable (y)
X = df.drop('Thermometer_Status', axis=1)
y = df['Thermometer_Status']

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
