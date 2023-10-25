import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset (replace 'your_dataset.csv' with the actual dataset file)
data = pd.read_csv('RTA Dataset1.csv')

# Specify the dependent variable (target) and independent variables (features)
dependent_variable = 'Severity'  # Replace with the actual column name
independent_variables = [
    'Weather', 
    'Road_Type',  
    'Num_Vehicles',
    'Speed_Limit',
    'Pedestrians',
    'Alcohol_Drugs',
]

# Split the data into training and testing sets
X = data[independent_variables]
y = data[dependent_variable]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f'Mean Absolute Error: {mae:.2f}')
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')

# Visualize the results (you can customize this part as needed)
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Severity")
plt.ylabel("Predicted Severity")
plt.title("Actual vs. Predicted Severity")
plt.show()

