import streamlit as st
import os
import pickle

# Define the class mapping
CLASS_MAPPING = {0:'Arabic', 1:'Danish', 2:'Dutch', 3:'English', 4:'French', 5:'German',
       6:'Greek', 7:'Hindi', 8:'Italian', 9:'Kannada', 10:'Malayalam', 11:'Portugeese',
       12:'Russian', 13:'Spanish', 14:'Sweedish', 15:'Tamil', 16:'Turkish'}

# Function to load the model
@st.cache_resource
def load_model():
    try:
        # Determine model file path
        model_path = os.path.join(os.path.dirname(__file__), "trained_pipeline-0.1.0.pkl")
        
        # Load model in binary mode
        with open(model_path, "rb") as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please upload the correct 'trained_pipeline-0.1.0.pkl' file.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        return None

# Load the model
model = load_model()

# Streamlit app interface
st.title("Language Detection App")
st.write("Enter a text snippet, and the model will detect the language.")

# Input text field
user_input = st.text_input("Input Text:")

# Predict language
if st.button("Detect Language"):
    if not model:
        st.error("Model is not loaded. Please check the logs for errors.")
    elif user_input.strip() == "":
        st.warning("Please enter some text to detect the language.")
    else:
        try:
            # Predict the class index
            class_index = model.predict([user_input])[0]
            
            # Get the corresponding language name
            detected_language = CLASS_MAPPING.get(class_index, "Unknown Language")
            
            st.success(f"The detected language is: **{detected_language}**")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
