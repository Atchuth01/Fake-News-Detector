import streamlit as st
import fasttext

# Load FastText Model
@st.cache_resource
def load_model():
    return fasttext.load_model("fasttext_model.bin")

model = load_model() 

# Streamlit UI
st.title("📰 Fake News Detector")
st.write("Enter a news article or headline to check if it's real or fake.")

# Text Input
news_text = st.text_area("Enter news text:", "")

# Predict Button
if st.button("Check News"):
    if news_text.strip():
        # Model Prediction
        label, prob = model.predict(news_text)
        result = "🟢 Real News" if label[0] == "__label__1" else "🔴 Fake News"

        # Display Result
        st.subheader("Result:")
        st.write(f"**Prediction:** {result}")
        st.write(f"**Confidence:** {prob[0] * 100:.2f}%")
    else:
        st.warning("⚠️ Please enter some text.")

# Run with: streamlit run app.py
