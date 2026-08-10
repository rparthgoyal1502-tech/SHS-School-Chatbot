import streamlit as st
from rapidfuzz import process

knowledge = {
    "hello": "👋 Hello! Welcome to SHS School. How can I help you?",
    "hi": "👋 Hi! Welcome to SHS School Chatbot.",
    "school timings": "🕐 SHS School timings are Monday to Friday, from 8:00 AM to 2:30 PM.",
    "timings": "🕐 School timings are Monday to Friday, from 8:00 AM to 2:30 PM.",
    "admission": "📝 For admission information, please contact the school office.",
    "fees": "💰 For the latest fee structure, please contact the accounts office.",
    "principal": "👩‍🏫 The Principal of SHS School is MRS. Vijaya Jeba Kumar.",
    "library": "📚 Library hours are from 8:30 AM to 3:00 PM.",
    "computer lab": "💻 SHS School has a modern computer lab with internet facilities.",
    "transport": "🚌 SHS School provides school bus transport facilities.",
    "board": "📘 SHS School follows the ICSE Board.",
    "sports": "🏏 SHS School provides facilities for various sports and activities.",
    "uniform": "👔 Students are required to wear the prescribed school uniform.",
    "exam": "📝 Examination information is provided according to the academic schedule.",
    "contact": "📞 Please contact the SHS School office for official contact information.",
    "address": "📍 Please contact the school office for the complete school address.",
    "website": "🌐 The ICSE Board website is cisce.org.",
    "bye": "👋 Goodbye! Thank you for using the SHS School Chatbot.",
    "thank you": "😊 You're welcome! I'm happy to help."
}

def get_answer(question):
    question = question.lower().strip()

    for key in knowledge:
        if key in question:
            return knowledge[key]

    result = process.extractOne(question, knowledge.keys())

    if result and result[1] >= 60:
        return knowledge[result[0]]

    return """🤖 Sorry, I couldn't find an answer to that.

You can ask me about:

🏫 School timings
📝 Admissions
💰 Fees
👩‍🏫 Principal
📚 Library
💻 Computer Lab
🚌 Transport
📘 Board
🏏 Sports
👔 Uniform
📝 Exams
📞 Contact
📍 Address"""

st.set_page_config(
    page_title="SHS School Chatbot",
    page_icon="🏫"
)

st.title("🏫 SHS SCHOOL CHATBOT")
st.subheader("Your School Information Assistant")
st.write("Ask questions about SHS School.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Type your question here...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    answer = get_answer(question)

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })