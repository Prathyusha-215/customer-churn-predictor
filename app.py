import os
import pickle
import streamlit as st
import numpy as np

# Set Streamlit page configuration
st.set_page_config(page_title="Customer Churn Prediction", page_icon="🔍", layout="wide")

# Custom CSS for an Attractive UI
st.markdown("""
    <style>
        /* Gradient Background */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #1f4037, #99f2c8);
            background-attachment: fixed;
            color: white;
        }

        /* Welcome Section */
        .welcome-container {
            text-align: center;
            padding: 100px 20px;
            animation: fadeIn 2s ease-in-out;
        }
        .title {
            font-size: 60px;
            font-weight: bold;
            text-shadow: 3px 3px 10px rgba(255, 255, 255, 0.4);
        }
        .description {
            font-size: 22px;
            margin-top: 20px;
            max-width: 800px;
            margin: auto;
            color: #E3E7EB;
        }
        /* Get Started Button */
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 40px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff9966, #ff5e62);
            color: white;
            font-size: 24px;
            font-weight: bold;
            border-radius: 50px;
            padding: 15px 60px;
            transition: 0.3s;
            box-shadow: 0px 5px 20px rgba(255, 94, 98, 0.5);
            border: none;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #ff5e62, #ff9966);
            transform: scale(1.1);
            box-shadow: 0px 10px 25px rgba(255, 94, 98, 0.7);
        }
        /* Result Styling */
        .result-container {
            text-align: center;
            margin-top: 30px;
        }
        .churn-yes {
            font-size: 24px;
            font-weight: bold;
            color: #FF4B2B;
            text-shadow: 2px 2px 5px rgba(255, 75, 43, 0.5);
        }
        .churn-no {
            font-size: 24px;
            font-weight: bold;
            color: #00C851;
            text-shadow: 2px 2px 5px rgba(0, 200, 81, 0.5);
        }
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
""", unsafe_allow_html=True)

# Navigation System
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# Welcome Page
if st.session_state.page == "welcome":
    st.markdown("""
        <div class="welcome-container">
            <h1 class="title">🔍 Customer Churn Prediction</h1>
            <p class="description">
                In today's fast-paced market, **customer retention is crucial**!  
                Our AI-powered **Churn Prediction System** helps businesses predict and prevent customer churn  
                using **advanced machine learning models**.  
                📊 **Enter customer details** and let AI **predict the risk of churn!**
            </p>
            <div class="button-container">
    """, unsafe_allow_html=True)

    # Get Started Button (Centered)
    if st.button("🚀 Get Started"):
        st.session_state.page = "prediction"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# Prediction Page
elif st.session_state.page == "prediction":
    st.markdown("<h1 style='text-align: center;'>📊 Predict Customer Churn</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar for Extra Features
    with st.sidebar:
        st.header("⚙️ Settings")
        show_decision_score = st.toggle("Show Decision Score", value=True)
        highlight_result = st.toggle("Highlight Prediction", value=True)

    # Input Fields
    st.markdown("### 📋 Enter Customer Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("🧑 Age", min_value=18, max_value=100, value=30, step=1)
        gender = st.radio("⚥ Gender", ["Male", "Female"])

    with col2:
        tenure = st.slider("📅 Tenure (months)", min_value=0, max_value=72, value=24, step=1)
        monthly_charges = st.number_input("💰 Monthly Charges ($)", min_value=0.0, step=0.1, value=50.0)

    # Convert gender to numerical
    gender = 1 if gender == "Female" else 0

    # Prepare input data
    input_data = np.array([[age, gender, tenure, monthly_charges]])

    # Load model
    model_path = "model.pkl"
    if not os.path.exists(model_path):
        st.error("⚠️ Model file not found! Please place 'model.pkl' in the correct directory.")
    else:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        st.success("✅ Model loaded successfully!")

        # Predict churn
        if st.button("🚀 Predict Churn"):
            prediction = model.predict(input_data)
            score = model.decision_function(input_data)  # SVC uses decision_function()

            if prediction[0] == 1:
                message = "❌ The customer is **likely to churn**."
                css_class = "churn-yes"
            else:
                message = "✅ The customer is **not likely to churn**."
                css_class = "churn-no"

            st.markdown(f"<div class='result-container'><p class='{css_class}'>{message}</p></div>", unsafe_allow_html=True)

            if show_decision_score:
                st.markdown(f"<div style='font-size:18px; text-align:center;'>📊 **Decision Score:** `{score[0]:.2f}`</div>", unsafe_allow_html=True)
