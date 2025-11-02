import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def download_dataset():
    """Download dataset from Kaggle if not exists"""
    if not os.path.exists("Crop_recommendation.csv"):
        print("📥 Dataset not found. Please download from:")
        print("https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset")
        print("Save as 'Crop_recommendation.csv' in this folder.")
        return False
    return True

def load_and_train_model():
    """Load dataset and train the model"""
    # Load the dataset
    data = pd.read_csv("Crop_recommendation.csv")
    print(f"📊 Dataset loaded: {data.shape[0]} samples, {data.shape[1]} features")
    
    # Separate features and target
    X = data.drop("label", axis=1)
    y = data["label"]
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Model initialization and training
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"✅ Model Accuracy: {accuracy:.2f}")
    
    return model

def get_user_input():
    """Get soil and climate parameters from user"""
    print("\n🌾 Crop Recommendation System")
    print("Enter the following soil and climate parameters:")
    
    n = float(input("Nitrogen (N): "))
    p = float(input("Phosphorus (P): "))
    k = float(input("Potassium (K): "))
    temperature = float(input("Temperature (°C): "))
    humidity = float(input("Humidity (%): "))
    ph = float(input("pH: "))
    rainfall = float(input("Rainfall (mm): "))
    
    return [n, p, k, temperature, humidity, ph, rainfall]

def predict_crop(model, user_input):
    """Predict and display recommended crop"""
    prediction = model.predict([user_input])
    print(f"\n🎯 Recommended Crop: {prediction[0]}")
    return prediction[0]

def main():
    """Main function"""
    if not download_dataset():
        return
    
    model = load_and_train_model()
    user_input = get_user_input()
    predict_crop(model, user_input)

if __name__ == "__main__":
    main()