# Customer Churn Prediction

## 📌 Project Overview
Customer churn is a critical issue for businesses, and predicting it can help companies take proactive measures to retain customers. This project uses a **machine learning model** to predict customer churn based on inputs like age, gender, tenure, and monthly charges.

The project is deployed using **Streamlit**, providing an interactive and visually appealing interface.

## 🚀 Features
- **User-Friendly Interface**: Modern UI with custom styling.
- **Machine Learning-Based Prediction**: Uses a pre-trained model to classify customer churn.
- **Real-Time Decision Score**: Displays the model's decision confidence.
- **Dynamic Input System**: Users can input relevant customer details to get a prediction.
- **Customizable Settings**: Options to highlight predictions and show decision scores.

## 🛠️ Tech Stack
- **Programming Language**: Python
- **Framework**: Streamlit
- **Machine Learning Model**: Pre-trained model using `pickle`
- **Libraries Used**:
  - `numpy` (for numerical computations)
  - `pickle` (for loading the model)
  - `os` (for file handling)
  - `streamlit` (for UI and deployment)

## 🛠️ Installation & Setup
### Prerequisites
Ensure you have Python installed along with the required dependencies.

### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/your-repo/customer-churn-prediction.git
 cd customer-churn-prediction
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```sh
streamlit run app.py
```

## 💁️ Project Structure
```
customer-churn-prediction/
│── model.pkl          # Pre-trained machine learning model
│── app.py             # Main Streamlit application
│── requirements.txt   # Dependencies
│── README.md          # Documentation
```

## 📊 How to Use
1. Open the application in a web browser.
2. Enter customer details like **age, gender, tenure, and monthly charges**.
3. Click on **Predict Churn**.
4. The result will show whether the customer is likely to churn or not.
5. Enable or disable **decision score** and **highlighted results** in the sidebar settings.

## ⚠️ Important Notes
- Ensure the **model.pkl** file is in the correct directory.
- The model must be compatible with the input format used in the app.

## 💡 Future Enhancements
- Adding more features like **customer location, service usage, and payment history**.
- Implementing deep learning models for improved accuracy.
- Connecting the app to a real-time database for automatic updates.

## 🤝 Contributing
We welcome contributions! Feel free to **fork** this repository, raise issues, and submit PRs.

## 📝 License
This project is **open-source** and available under the MIT License.

---

