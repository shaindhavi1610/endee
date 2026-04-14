import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

st.title("🚀 SkillBridge AI")

st.write("Enter your skills (comma separated):")

user_input = st.text_input("Your Skills")

# Sample job skills dataset
job_roles = {
    "Data Scientist": ["python", "machine learning", "data analysis", "pandas"],
    "Web Developer": ["html", "css", "javascript", "react"],
    "AI Engineer": ["python", "deep learning", "nlp", "tensorflow"]
}

def text_to_vector(text):
    words = text.lower().split(",")
    return list(set([w.strip() for w in words]))

def similarity(user, job):
    common = set(user).intersection(set(job))
    return len(common) / len(set(job))

if st.button("Analyze"):
    user_skills = text_to_vector(user_input)
    results = {}

    for role, skills in job_roles.items():
        score = similarity(user_skills, skills)
        results[role] = score

    best_match = max(results, key=results.get)

    st.subheader("🔍 Results")
    for role, score in results.items():
        st.write(f"{role}: {round(score*100,2)}% match")

    st.success(f"Best Match: {best_match}")
