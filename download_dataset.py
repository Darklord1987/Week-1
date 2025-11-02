import os
import requests
import zipfile

def download_kaggle_dataset():
    try:
        import kaggle
        print("📥 Downloading dataset from Kaggle...")
        kaggle.api.dataset_download_files('atharvaingle/crop-recommendation-dataset', 
                                         path='.', unzip=True)
        print("✅ Dataset downloaded successfully!")
        return True
    except ImportError:
        print("❌ Kaggle API not installed. Install with: pip install kaggle")
        print("📋 Manual download instructions:")
        print("1. Go to: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset")
        print("2. Download the dataset")
        print("3. Extract and place 'Crop_recommendation.csv' in this folder")
        return False
    except Exception as e:
        print(f"❌ Error downloading: {e}")
        return False

if __name__ == "__main__":
    download_kaggle_dataset()