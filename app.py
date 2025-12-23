import os
import streamlit as st
from prediction import predict

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Car Damage Detection",
    page_icon="🚗",
    layout="centered"
)

# ===================== SIDEBAR =====================
with st.sidebar:
    st.title("📌 Project Info")

    with st.expander("📖 Project Overview"):
        st.markdown(
            """
            **Car Damage Detection App** built using **Streamlit** and a  
            **ResNet50 deep learning model**.

            - Classifies vehicle damage into **6 categories**
            - Uses **transfer learning** with pre-trained ResNet50 weights
            - Trained on **2,300 labeled car images**
            - Achieved **~80% validation accuracy**
            - Robust to lighting, rotation, and contrast variations
            """
        )

    with st.expander("🛠️ Tech Stack"):
        st.markdown(
            """
            **Backend**
            - Python
            - PyTorch
            - TorchVision

            **Modeling & Evaluation**
            - Transfer Learning (ResNet50)
            - Scikit-learn
            - Matplotlib
            - Optuna

            **Deployment**
            - Streamlit
            - Streamlit Cloud
            """
        )

    with st.expander("🧠 Damage Categories"):
        st.markdown(
            """
            - Front Normal  
            - Front Breakage  
            - Front Crushed  
            - Rear Normal  
            - Rear Breakage  
            - Rear Crushed  
            """
        )

# ===================== MAIN UI =====================
st.title("🚗 Car Damage Detection System")
st.subheader(" vehicle damage classification using Deep Learning")

st.markdown(
    """
    Upload an image of a vehicle to automatically classify  
    the **type and severity of damage**.
    """
)

st.divider()

# ---------------- Image Upload Section ----------------
st.header("📤 Upload Vehicle Image(s)")

UPLOAD_DIR = "/tmp/Uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

uploaded_files = st.file_uploader(
    "Choose image files",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

# ---------------- Prediction Section ----------------
if uploaded_files:
    st.subheader("🔍 Prediction Results")

    for image_file in uploaded_files:
        image_path = os.path.join(UPLOAD_DIR, image_file.name)

        with open(image_path, "wb") as file:
            file.write(image_file.getbuffer())

        with st.container():
            st.image(image_file, caption=image_file.name, use_container_width=True)

            try:
                prediction = predict(image_path)
                st.success(f"**Predicted Damage Type:** {prediction}")
            except Exception as e:
                st.error(f"Prediction error: {e}")

# ---------------- Footer ----------------
st.divider()
st.caption(
    "⚠️ Disclaimer: This model may make incorrect predictions. "
    "Use results as a supporting tool, not a final assessment."
)
