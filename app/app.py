import streamlit as st
import pickle
import os
from pathlib import Path

# Set page config
st.set_page_config(page_title="AutoJudge", layout="centered")

@st.cache_resource
def load_models():
    """Load the pre-trained models."""
    try:
        models_dir = Path(r"C:\Users\sonia\Desktop\acm_open_project\models")
        return {
            'vectorizer': pickle.load(open(r"C:\Users\sonia\Desktop\acm_open_project\models\tfidf.pkl", "rb")),
            'classifier': pickle.load(open(r"C:\Users\sonia\Desktop\acm_open_project\models\classifier.pkl", "rb")),
            'regressor': pickle.load(open(r"C:\Users\sonia\Desktop\acm_open_project\models\regressor.pkl", "rb"))
        }
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None

def main():
    st.title("AutoJudge - Problem Difficulty Predictor")
    st.write("Enter the problem details to predict its difficulty.")
    
    # Load models
    models = load_models()
    if models is None:
        st.stop()
    
    # Input fields
    desc = st.text_area("Problem Description", height=150)
    inp = st.text_area("Input Description", height=100)
    out = st.text_area("Output Description", height=100)
    
    if st.button("Predict Difficulty"):
        if not all([desc, inp, out]):
            st.warning("Please fill in all fields")
            return
            
        with st.spinner("Analyzing problem..."):
            try:
                # Combine and preprocess text
                text = f"{desc} {inp} {out}".lower()
                
                # Make predictions
                vec = models['vectorizer'].transform([text])
                difficulty = models['classifier'].predict(vec)[0]
                score = models['regressor'].predict(vec)[0]
                
                # Display results
                st.success("### Prediction Results")
                st.write(f"**Difficulty Class:** {difficulty}")
                st.write(f"**Difficulty Score:** {score:.2f}/10.0")
                
            except Exception as e:
                st.error(f"Error making prediction: {str(e)}")

if __name__ == "__main__":
    main()
