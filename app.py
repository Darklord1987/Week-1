import streamlit as st
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

@st.cache_data
def load_data():
    """Load and cache the dataset"""
    if not os.path.exists("Crop_recommendation.csv"):
        st.error("Dataset not found! Please download Crop_recommendation.csv")
        st.stop()
    return pd.read_csv("Crop_recommendation.csv")

@st.cache_resource
def train_model():
    """Train and cache the model"""
    data = load_data()
    X = data.drop("label", axis=1)
    y = data["label"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    accuracy = accuracy_score(y_test, model.predict(X_test))
    return model, accuracy

def main():
    st.set_page_config(page_title="🌾 Crop Recommendation", layout="wide")
    
    st.title("🌾 Crop Recommendation System")
    st.markdown("**Sustainable Agriculture with AI** - Get crop recommendations based on soil and climate data")
    
    # Load model
    model, accuracy = train_model()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📊 Enter Soil & Climate Parameters")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            n = st.number_input("Nitrogen (N)", min_value=0.0, max_value=200.0, value=50.0)
            p = st.number_input("Phosphorus (P)", min_value=0.0, max_value=200.0, value=50.0)
            k = st.number_input("Potassium (K)", min_value=0.0, max_value=200.0, value=50.0)
            temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
        
        with col_b:
            humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)
            ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0)
            rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0)
        
        if st.button("🎯 Get Crop Recommendation", type="primary"):
            user_input = [[n, p, k, temperature, humidity, ph, rainfall]]
            prediction = model.predict(user_input)[0]
            
            st.success(f"🌱 **Recommended Crop: {prediction.upper()}**")
    
    with col2:
        st.subheader("📈 Model Info")
        st.metric("Model Accuracy", f"{accuracy:.1%}")
        
        st.subheader("🌱 About")
        st.info("""
        This system uses machine learning to recommend crops based on:
        - Soil nutrients (N, P, K)
        - Climate conditions
        - pH levels
        
        **Goal:** Support sustainable agriculture (SDG 2 - Zero Hunger)
        """)

if __name__ == "__main__":
    main()