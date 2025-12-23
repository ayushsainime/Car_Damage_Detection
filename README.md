# 🚗 Car Damage Detection using Deep Learning

An AI-powered web application that automatically classifies vehicle damage from images using a deep learning model based on **ResNet50**.  
Built with **PyTorch** and deployed using **Streamlit**, this project aims to assist users, insurance companies, and inspection teams in quickly assessing vehicle damage.

---

<img width="1916" height="920" alt="Screenshot 2025-12-23 213755" src="https://github.com/user-attachments/assets/3259ab5c-4e84-45f3-a62e-0ca274b0160c" />

<img width="1919" height="915" alt="Screenshot 2025-12-23 213913" src="https://github.com/user-attachments/assets/fdfb7be1-8ea3-4ab3-ac6d-08e296f13f95" />



## 📌 Project Overview

The **Car Damage Detection App** allows users to upload images of damaged vehicles and receive instant predictions about the type and severity of damage.

### 🔍 Key Features
- Classifies vehicle damage into **six distinct categories**
- Uses **transfer learning** with pre-trained **ResNet50**
- Robust against variations in **lighting, rotation, and contrast**
- Simple and intuitive **Streamlit-based UI**
- Deployed and ready to run on **Streamlit Cloud**

---

## 🧠 Damage Categories

The model predicts one of the following classes:

- Front Normal  
- Front Breakage  
- Front Crushed  
- Rear Normal  
- Rear Breakage  
- Rear Crushed  

---

## 📊 Model Details

- **Architecture:** ResNet50 (Transfer Learning)
- **Framework:** PyTorch
- **Dataset Size:** ~2,300 labeled vehicle images
- **Validation Accuracy:** ~80%
- **Data Augmentation Techniques:**
  - Random rotations
  - Color jitter
  - Contrast variation
  - Image normalization

The model was fine-tuned on a diverse dataset to improve generalization across real-world conditions.

---

## 🛠️ Tech Stack

### Backend & Modeling
- Python
- PyTorch
- TorchVision

### Evaluation & Optimization
- Scikit-learn
- Matplotlib
- Optuna

### Deployment
- Streamlit

🚀 How to Run the Project Locally
1️⃣ Clone the Repository
```
git clone https://github.com/your-username/car-damage-detection.git
cd car-damage-detection
```

2️⃣ Create a Virtual Environment (Optional but Recommended)
```
python -m venv venv
venv\Scripts\activate
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

4️⃣ Run the Streamlit App
```
streamlit run app.py
```

The app will open in your browser at:
```
http://localhost:8501
```
