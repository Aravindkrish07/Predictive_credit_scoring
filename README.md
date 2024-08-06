# Predictive Credit Scoring

This project is a predictive credit scoring application built using machine learning and Flask. It employs a RandomForestClassifier to predict the likelihood of loan repayment based on various features of the borrower. The predictions are then stored in a PostgreSQL database for further analysis.

## Project Overview

The main goal of this project is to create a predictive model that helps financial institutions assess the credit risk of potential borrowers. By analyzing various features such as the borrower's credit history, loan amount, and other financial indicators, the model predicts whether the borrower is likely to repay the loan.

### Features

- **Data Preprocessing**: Handling missing values, encoding categorical variables, and scaling numerical features.
- **Model Building**: Training a RandomForestClassifier model to predict loan repayment likelihood.
- **API Development**: Developing a Flask API to serve the model and handle prediction requests.
- **Database Integration**: Storing predictions in a PostgreSQL database for further analysis.

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- Git

### Steps

1. **Clone the Repository:**
2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up PostgreSQL:**

    - Create a PostgreSQL database named `credit_scoring`.
    - Create a table `predictions` with the following schema:

    ```sql
    CREATE TABLE predictions (
        id SERIAL PRIMARY KEY,
        features JSONB,
        prediction INT
    );
    ```

5. **Run the Flask Application:**

    ```bash
    python app.py
    ```

6. **Test the API:**

    - Use Postman or any other API client to send POST requests to `http://127.0.0.1:5000/predict` with the required JSON payload.

## Project Structure

- `app.py`: Flask application file that handles incoming prediction requests and saves the results to PostgreSQL.
- `data_preprocessing.py`: Script for data preprocessing, including handling missing values, encoding categorical variables, and scaling numerical features.
- `model_training.py`: Script for training the machine learning model.
- `convert_to_csv.py`: Script for converting the dataset to CSV format.
- `requirements.txt`: List of dependencies required to run the project.
- `README.md`: Project documentation.

## Usage

### Running the Application

1. **Start the Flask Application:**

    ```bash
    python app.py
    ```

2. **Send a Prediction Request:**

    Use Postman or any HTTP client to send a POST request to `http://127.0.0.1:5000/predict` with a JSON payload in the following format:

    ```json
    {
        "features": {
            "Status of existing checking account": "A11",
            "Duration in months": 6,
            "Credit history": "A34",
            "Purpose": "A43",
            "Credit amount": 1169,
            "Savings account/bonds": "A65",
            "Present employment since": "A75",
            "Installment rate in percentage of disposable income": 4,
            "Personal status and sex": "A93",
            "Other debtors / guarantors": "A101",
            "Present residence since": 4,
            "Property": "A121",
            "Age in years": 67,
            "Other installment plans": "A143",
            "Housing": "A152",
            "Number of existing credits at this bank": 2,
            "Job": "A173",
            "Number of people being liable to provide maintenance for": 1,
            "Telephone": "A192",
            "Foreign worker": "A201"
        }
    }
    ```

3. **Check the Database:**

    Verify that the prediction has been saved to the `predictions` table in your PostgreSQL database.

## Contributing

1. **Fork the repository.**
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Make your changes.**
4. **Commit your changes** (`git commit -m 'Add some feature'`).
5. **Push to the branch** (`git push origin feature-branch`).
6. **Open a pull request**.

