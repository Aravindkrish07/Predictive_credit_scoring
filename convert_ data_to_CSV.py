# import pandas as pd
#
# # Define the column names based on the dataset description
# column_names = [
#     'Status of existing checking account', 'Duration in months', 'Credit history',
#     'Purpose', 'Credit amount', 'Savings account/bonds', 'Present employment since',
#     'Installment rate in percentage of disposable income', 'Personal status and sex',
#     'Other debtors / guarantors', 'Present residence since', 'Property', 'Age in years',
#     'Other installment plans', 'Housing', 'Number of existing credits at this bank',
#     'Job', 'Number of people being liable to provide maintenance for', 'Telephone', 'Foreign worker', 'Cost Matrix(Risk)'
# ]
#
# # Load the dataset
# data = pd.read_csv('german.data', delim_whitespace=True, header=None, names=column_names)
#
# # Save the dataset as CSV
# data.to_csv('german_credit_data.csv', index=False)


import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

# Load dataset
data = pd.read_csv('german_credit_data.csv')

# Handle missing values (if any)
data.ffill(inplace=True)

# Encode categorical variables
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])

# Save label encoders
joblib.dump(label_encoders, 'label_encoders.pkl')

# Scale numerical features except the target column
scaler = StandardScaler()
numerical_features = data.select_dtypes(include=['int64', 'float64']).columns.drop('Cost Matrix(Risk)')
data[numerical_features] = scaler.fit_transform(data[numerical_features])

# Save scaler
joblib.dump(scaler, 'scaler.pkl')

# Save preprocessed data
data.to_csv('preprocessed_credit_data.csv', index=False)

# Print the first few rows of the preprocessed data
print(data.head())
print(data.info())
print(data.describe())
