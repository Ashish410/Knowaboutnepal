import streamlit as st

# Page setup
st.set_page_config(page_title="Nepal Quiz 🇳🇵", page_icon="🗻", layout="centered")

# Title and intro
st.title("Know about 🇳🇵")
st.markdown("**Created by: Ashish ✨**")

#  full list of questions
questions = [
    {
        "question": "what is the  capital city of Nepal?",
        "options": ["A. Kathmandu", "B. Bhaktapur ", "C. Lalitpur",  "D. Gorkha"],
        "answer": "A"
    },
    {
        "question": "What is the highest Mountain of Nepal?",
        "options": [ "A. Mount Kanchenjunga", "B. Mount Annapurna", "C. Mount Everest", "D. Mount Dhaulagiri"],
        "answer": "C"
    },
    {
        "question": "Which river is the longest in Nepal?",
        "options": ["A. Gandaki", "B. Bagmati", "C. Karnali", "D. Koshi"],
        "answer": "C"
    },
    {
        "question": "Which city is known as the gateway of Nepal?",
        "options": [ "A. Namche Bazaar", "B. Lukla", "C. Pokhara", "D. Kathmandu"],
        "answer": "B"
    },
    {
        "question": "What is the name of the flat southern region of Nepal?",
        "options": [ "A. Hill region", "B. Mid-westen region", "C. Terai Region", "D. Mountain region"],
        "answer": "C"
    },
    {
        "question": "Which Lake is the second largest in Nepal and a popular tourist destination?",
        "options": [ "A. Phewa Lake", "B. Begnas Lake", "C. Tilicho Lake", "D. Rara Lake"],
        "answer": "A"
    },
    {
        "question": "Which national park in Nepal is a UNESCO world heritage site and home to Bengal tigers?",
        "options": [ "A. Langtang National Park", "B. Chitwan National Park", "C. Rara National Park", "C. Sagarmatha National Park"],
        "answer": "B"
    },
    {
        "question": "Which mountain range froms the northern border of Nepal?",
        "options": [ "A. Himalayas", "B. Alps", "C. Rockies", "D. Andes"],
        "answer": "A"
    },
    {
        "question": "Which valley is considered the cultural and historical heart of Nepal?",
        "options": [ "A. Solukhumbu Valley", "B. Pokhara Valley", "C. Kathmandu Valley", "D. Terai Valley"],
        "answer": "C"
    },
    {
        "question": "Which region of Nepal is most prone to landslide and eroison due to steep terrain?",
        "options": [ "A. Mountain Region", "B. Hill Region", "C. Terai Region", "D. Mid-western Region"],
        "answer": "B"
    },
    {
        "question": "Which river basin is crucial for hydroelectric power generation in Nepal?",
        "options": [ "A. Bagmati Basin", "B. Karnali Basin", "C. Gandaki Basin", "D. Koshi Basin"],
        "answer": "C"
    }
]

# Quiz form
with st.form("quiz_form"):
    st.subheader("Choose your answers:")
    user_answers = {}
    for i, data in enumerate(questions):
        q = data["question"]
        user_answers[q] = st.radio(q, ["Choose an answer"] + data["options"], index=0, key=f"q{i}")
    submitted = st.form_submit_button("Submit")

# Score evaluation
if submitted:
    score = 0
    st.subheader("Results:")
    for data in questions:
        q = data["question"]
        selected = user_answers[q]
        correct = next(opt for opt in data["options"] if opt.startswith(data["answer"] + "."))
        if selected == correct:
            st.success(f"✅ {q} — Correct!")
            score += 1
        elif selected == "Choose an answer":
            st.warning(f"⚠️ {q} — No answer selected. Correct answer: {correct}")
        else:
            st.error(f"❌ {q} — Wrong! Correct answer: {correct}")
    st.markdown(f"### Your final score: **{score} / {len(questions)}**")

    # Replay button
    if st.button("Play Again"):
        st.experimental_rerun()
