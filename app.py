import streamlit as st
import pickle

# Load the model
with open('train_pipeline-0.1.0.pkl', 'rb') as file:
    model = pickle.load(file)

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

# Predict language
if st.button("Detect Language"):
    if user_input.strip() == "":
        st.warning("Please enter some text to detect the language.")
    else:
        try:
            # Predict the class index
            class_index = model.predict([user_input])[0]
            
            # Get the corresponding language name
            detected_language = CLASS_MAPPING.get(class_index, "Unknown Language")
            
            st.success(f"The detected language is: **{detected_language}**")
        except Exception as e:
            st.error(f"An error occurred: {e}")
