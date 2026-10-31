import streamlit as st
from predict import predict

st.set_page_config(page_title="Fake News Detector", page_icon="📰")
st.title("📰 Fake News Detection using NLP")
st.caption("ABESEC | IT Final Year Project")

title = st.text_input("News headline (optional)")
body = st.text_area("News article text", height=250)

if st.button("Check"):
    content = f"{title} {body}".strip()
    if len(content.split()) < 5:
        st.warning("Please enter a longer piece of text.")
    else:
        label, conf = predict(content)
        if label == "Real":
            st.success("✅ Likely REAL news")
        else:
            st.error("🚨 Likely FAKE news")
        if conf is not None:
            st.progress(min(conf, 1.0), text=f"Confidence: {conf*100:.1f}%")
        st.info("This is a statistical model based on writing patterns. Always verify with trusted sources.")
