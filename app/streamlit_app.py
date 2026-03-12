import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide"
)

# ---------- Styling ----------
st.markdown("""
    <style>
    .stApp {
        background-color: #F8FAFC;
        color: #0F172A;
    }

    .main-title {
        font-size: 40px;
        font-weight: 700;
        color: #0F766E;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        font-size: 18px;
        color: #475569;
        margin-bottom: 1.5rem;
    }

    .result-card {
        background-color: white;
        padding: 24px;
        border-radius: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        margin-top: 10px;
    }

    .risk-low {
        color: #15803D;
        font-weight: 700;
    }

    .risk-medium {
        color: #B45309;
        font-weight: 700;
    }

    .risk-high {
        color: #B91C1C;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Main Page ----------
st.markdown('<div class="main-title">Customer Churn Prediction System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Predict churn risk and support customer retention decisions using machine learning.</div>',
    unsafe_allow_html=True
)

st.sidebar.header("Customer Inputs")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
Partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
Dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
tenure = st.sidebar.number_input("Tenure", min_value=0, value=12)
PhoneService = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.sidebar.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.sidebar.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.sidebar.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.sidebar.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.sidebar.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.sidebar.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.sidebar.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
Contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.sidebar.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)
MonthlyCharges = st.sidebar.number_input("Monthly Charges", min_value=0.0, value=65.5)
TotalCharges = st.sidebar.number_input("Total Charges", min_value=0.0, value=786.0)

predict_btn = st.sidebar.button("Predict Churn Risk")

# ---------- Result Section ----------
if predict_btn:
    payload = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)

        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            probability = float(result["probability"])

            if probability < 0.35:
                risk_level = "Low"
                risk_class = "risk-low"
                recommendation = "Customer risk is low. No urgent retention action is needed."
            elif probability < 0.65:
                risk_level = "Medium"
                risk_class = "risk-medium"
                recommendation = "Customer risk is moderate. Consider follow-up communication or a retention offer."
            else:
                risk_level = "High"
                risk_class = "risk-high"
                recommendation = "Customer risk is high. Recommend immediate retention action or a personalized offer."

            factors = []
            if tenure < 12:
                factors.append("Short customer tenure")
            if Contract == "Month-to-month":
                factors.append("Month-to-month contract")
            if MonthlyCharges > 70:
                factors.append("Higher monthly charges")
            if InternetService == "Fiber optic":
                factors.append("Fiber optic service")

            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.subheader("Prediction Result")
            st.write(f"**Prediction:** {prediction}")
            st.write(f"**Probability:** {probability:.2f}")
            st.markdown(f'**Risk Level:** <span class="{risk_class}">{risk_level}</span>', unsafe_allow_html=True)
            st.progress(min(max(probability, 0.0), 1.0))

            st.subheader("Recommendation")
            st.info(recommendation)

            st.subheader("Possible Risk Factors")
            if factors:
                for factor in factors:
                    st.write(f"- {factor}")
            else:
                st.write("No strong risk factors identified from the current input.")

            st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.error("API request failed.")

    except Exception as e:
        st.error(f"Connection error: {e}")

else:
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.subheader("How to use")
    st.write("Use the sidebar to enter customer information, then click **Predict Churn Risk**.")
    st.markdown('</div>', unsafe_allow_html=True)