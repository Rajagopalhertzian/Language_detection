import streamlit as st
import pickle
import os

# Path to the model file
MODEL_PATH = os.path.join(os.path.dirname(__file__), "train_pipeline-0.1.0.pkl")

# Load the trained model
try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Ensure 'train_pipeline-0.1.0.pkl' is in the same directory as this script.")
    st.stop()

# Define the class mapping
CLASS_MAPPING = {
    0: "English",
    1: "Hindi",
    2: "French",
    3: "Spanish",
    4: "German",
    5: "Chinese",
    6: "Japanese",
    7: "Russian",
    8: "Korean",
    9: "Arabic",
    10: "Portuguese"
}

# Streamlit app
st.title("Language Detection App")
st.write("Enter a text snippet, and the model will detect the language.")

# Input text field
user_input = st.text_input("Input Text:")

# Detect Language Button
if st.button("Detect Language"):
    if not user_input.strip():
        st.warning("Please enter some text to detect the language.")
    else:
        try:
            # Predict the class index
            class_index = model.predict([user_input])[0]
            
            # Get the corresponding language name
            detected_language = CLASS_MAPPING.get(class_index, "Unknown Language")
            
            # Display the result
            st.success(f"The detected language is: **{detected_language}**")
        except Exception as e:
            st.error(f"An error occurred: {e}")
