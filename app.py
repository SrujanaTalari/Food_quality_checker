import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from image_model import create_model
from nlp_model import predict_complaint
from quality_score import calculate_quality_score
import tensorflow as tf

# Load image model
model = create_model()

st.title("🍱 Intelligent Food Delivery Quality Checker")

# Upload food image
uploaded_file = st.file_uploader("Upload Food Image", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).resize((128,128))
    st.image(image, caption="Uploaded Image")

    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    image_quality = "Good" if prediction[0][0] > 0.5 else "Bad"

    st.subheader("Image Quality Result:")
    st.write(image_quality)

# Complaint Input
complaint_text = st.text_area("Enter Customer Complaint")

if complaint_text:
    complaint_quality = predict_complaint(complaint_text)

    st.subheader("Complaint Analysis:")
    st.write(complaint_quality)

# Score Calculation
if uploaded_file and complaint_text:
    final_score = calculate_quality_score(image_quality, complaint_quality)

    st.subheader("Overall Quality Score:")
    st.write(final_score)

    # Visualization
    st.subheader("Quality Visualization")

    categories = ['Image Quality', 'Complaint Quality']
    values = [50 if image_quality=="Good" else 10,
              50 if complaint_quality=="Good" else 10]

    plt.bar(categories, values)
    st.pyplot(plt)