from sklearn.model_selection import train_test_split
import pandas as pd

# Load preprocessed data
data = pd.read_csv('preprocessed_credit_data.csv')

# Split data into features and target
X = data.drop('Cost Matrix(Risk)', axis=1)  # Replace 'Cost Matrix(Risk)' with your actual target column name
y = data['Cost Matrix(Risk)']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the split data
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)
