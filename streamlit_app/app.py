import streamlit as st
from PIL import Image
import os

st.title("Image Analysis Pipeline")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Processing...")

    # Save uploaded image
    image_path = f"../data/input_images/{uploaded_file.name}"
    image.save(image_path)
    
    # Run the pipeline (example for segmentation)
    from models.segmentation_model import segment_image
    image, prediction = segment_image(image_path)
    
    from utils.preprocessing import extract_objects
    extract_objects(np.array(image), prediction, "../data/segmented_objects/")
    
    st.write("Segmentation complete.")
    st.image(image, caption='Segmented Image.', use_column_width=True)
    
    # Further steps can be added similarly
