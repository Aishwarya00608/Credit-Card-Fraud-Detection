# Real-Time Credit Card Fraud Detection

## Description
This project demonstrates a complete machine learning pipeline for detecting fraudulent credit card transactions in real-time. The primary challenge is handling a highly imbalanced dataset. The final output is a Flask API that can classify a transaction as fraudulent or normal.

---

## Dataset
The project uses the "Credit Card Fraud Detection" dataset from Kaggle.
[Link to dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

---

## How to Run the Project

1.  **Clone the Repository (or download the files).**

2.  **Install Dependencies:**
    Open a terminal in the project folder and run the following command to install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Start the API Server:**
    In the same terminal, start the real-time alert system:
    ```bash
    python app.py
    ```
    The server will be running at `http://127.0.0.1:5000`.

4.  **Test the API:**
    Open a **second, separate terminal**. In this new terminal, run the test script to send a sample transaction to the server:
    ```bash
    python test_api.py
    ```
    The terminal will print the server's JSON response.

---

## Results
The project trained several models, with the Random Forest Classifier providing the best balance of precision and recall. The model was successfully deployed as a real-time API capable of flagging suspicious transactions.