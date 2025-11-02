# Crop Recommendation System 🌾

## 📝 Description
A beginner-friendly machine learning project for sustainability.
The program recommends which crop a farmer should grow based on soil and climate features like nitrogen (N), phosphorus (P), potassium (K), temperature, humidity, pH, and rainfall.

## 📂 Project Structure
```
crop_recommendation/
│
├── 🌐 app.py                    # Streamlit web interface
├── 🐍 crop_model.py             # Command-line version
├── 📥 download_dataset.py        # Kaggle dataset downloader
├── 📋 requirements.txt           # Python dependencies
├── 📊 Crop_recommendation.csv    # Dataset (after download)
└── 📖 README.md                  # This file
```

## 📊 Dataset
[Crop Recommendation Dataset – Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

## 🚀 Steps to Run

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Download Dataset
**🤖 Method A - Automatic (Kaggle API):**
```bash
python download_dataset.py
```

**📎 Method B - Manual:**
- Go to: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset
- Download and extract `Crop_recommendation.csv` to this folder

### 3️⃣ Run the System
**🌐 Web App (Recommended):**
```bash
streamlit run app.py
```

**⌨️ Command Line:**
```bash
python crop_model.py
```

### 4️⃣ Get Results
📊 Enter soil and climate parameters → 🎯 Get your recommended crop!

## 🌍 Sustainability Goal
Supports **SDG Goal 2 – Zero Hunger** by promoting smart and efficient agriculture 🌱

## 🏆 Project Status
✅ **100% Complete** - Fully functional crop recommendation system

### ✨ Features:
- ✅ 📊 Dataset loading and validation
- ✅ 🤖 Machine learning model training (Decision Tree)
- ✅ 📈 Model accuracy evaluation  
- ✅ 📝 Interactive user input collection
- ✅ 🎯 Crop prediction and recommendation
- ✅ 📥 Kaggle dataset integration
- ✅ 🌐 **Streamlit Web Interface**

---

📞 **Made with ❤️ for sustainable agriculture** 🌾