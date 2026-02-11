# 🏠 House Price Prediction - Linear Regression

> 📈 Machine Learning solution for predicting house prices using **Linear Regression**. Features a complete pipeline from data preprocessing to an interactive **Streamlit** web interface.

[![GitHub](https://img.shields.io/badge/GitHub-ryujin05-blue?logo=github)](https://github.com/ryujin05)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

---

## ✨ Key Features

- 📊 **Predictive Modeling** - Accurate price estimation using Linear Regression algorithms.
- 🧹 **Data Pipeline** - Comprehensive preprocessing including missing value handling and feature selection.
- 🌐 **Interactive Web UI** - User-friendly dashboard for real-time price prediction.
- 💾 **Model Persistence** - Efficient model saving and loading using `joblib` for production readiness.

---

## 🏗️ Architecture

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.x |
| **ML Library** | Scikit-learn |
| **Data Analysis** | Pandas |
| **Web Framework** | Streamlit |

---

## 📁 Directory Structure

```text
.
├── train.csv          # 📊 Training dataset 
├── predict.py            # 🧠 Model training & preprocessing script
├── app.py                # 🎨 Streamlit web application
├── house_model.pkl       # 💾 Serialized ML model
└── features_list.pkl     # 📋 Saved feature metadata
---
```

### Prerequisites
- Python 3.8+
- pip (Python package manager)
```
### Installation

```bash
pip install pandas scikit-learn streamlit joblib
Running the Project
1️⃣ Train the Model
Generate the model file by running the training script:

Bash
python predict.py
2️⃣ Launch Web App
Start the interactive Streamlit interface:

Bash
python -m streamlit run app.py
```
🎥 Live Demo
Watch the full project demo here: [Google Drive Link](https://drive.google.com/file/d/1QqLVPaedLfSKfOVnxq4IYx_LVkhX1euk/view?usp=sharing)
```
  
```
<div align="center">

</div>

👨‍💻 Author
<div align="center">

Pham The Dat  IT Student  at Hanoi University of Science and Technology (HUST)

</div>
Made with ❤️ by Pham The Dat

⭐ If you found this project useful, please consider giving it a star on GitHub!

</div>
