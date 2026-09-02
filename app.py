import streamlit as st
import time
import os

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="SHS School Chatbot",
    page_icon="🏫",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# SCHOOL INFORMATION
# ============================================================

SCHOOL_NAME = "Sacred Heart School, Moga"

ADDRESS = "Dosanj Road, Moga, Punjab - 142001"

PRINCIPAL = "Mrs. Vijaya Jeba Kumar"

SCHOOL_TIMING = "7:50 AM to 2:30 PM"

BOARD = "ICSE"

SCHOOL_WEBSITE = "https://shsmoga.com/"

CISCE_WEBSITE = "https://cisce.org/"

PHONE = "01636-239777"

EMAIL_PRINCIPAL = "emailprincipal@shsmoga.com"
EMAIL_ADMIN = "admin@shsmoga.com"
EMAIL_FEEDBACK = "feedback@shsmoga.com"


# ============================================================
# DARK CLASSY DESIGN
# ============================================================

st.markdown(
    """
    <style>

    /* ============================= */
    /* MAIN BACKGROUND */
    /* ============================= */

    .stApp {
        background: #0b0b0b;
        color: #ffffff;
    }

    [data-testid="stAppViewContainer"] {
        background: #0b0b0b;
    }

    [data-testid="stHeader"] {
        background: #0b0b0b;
    }

    .main .block-container {
        max-width: 900px;
        padding-top: 1.5rem;
        padding-bottom: 7rem;
    }


    /* ============================= */
    /* SCHOOL HEADER */
    /* ============================= */

    .school-header {
        text-align: center;
        margin-bottom: 25px;
    }

    .school-title {
        font-size: 36px;
        font-weight: 800;
        letter-spacing: 1px;
        color: #ffffff;
        margin-top: 10px;
    }

    .school-subtitle {
        font-size: 16px;
        color: #bdbdbd;
        margin-top: 5px;
    }

    .gold-line {
        width: 120px;
        height: 3px;
        background: #d4af37;
        margin: 12px auto 0 auto;
        border-radius: 10px;
    }


    /* ============================= */
    /* LOGO */
    /* ============================= */

    .logo-box {
        text-align: center;
        margin-bottom: 5px;
    }

    .logo-box img {
        width: 145px;
        height: 145px;
        object-fit: contain;
        border-radius: 50%;
    }


    /* ============================= */
    /* CHAT MESSAGE */
    /* ============================= */

    [data-testid="stChatMessage"] {
        background: transparent !important;
        border: none !important;
        padding: 5px 0;
    }


    /* ============================= */
    /* CHAT INPUT */
    /* ============================= */

    [data-testid="stChatInput"] {
        background: #151515 !important;
        border: 1px solid #333333 !important;
        border-radius: 18px !important;
    }

    [data-testid="stChatInput"] textarea {
        background: #151515 !important;
        color: #ffffff !important;
        border: none !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #888888 !important;
    }


    /* ============================= */
    /* THINKING ANIMATION */
    /* ============================= */

    .thinking-box {
        background: #181818;
        border: 1px solid #2d2d2d;
        border-radius: 15px;
        padding: 12px 18px;
        display: inline-block;
        color: #aaaaaa;
        font-size: 15px;
    }

    .thinking-dots {
        display: inline-block;
        min-width: 25px;
    }


    /* ============================= */
    /* INFO BOX */
    /* ============================= */

    .info-box {
        background: #141414;
        border: 1px solid #292929;
        border-radius: 15px;
        padding: 15px;
        margin-top: 10px;
        color: #cccccc;
    }


    /* ============================= */
    /* MOBILE */
    /* ============================= */

    @media (max-width: 600px) {

        .main .block-container {
            padding-left: 12px;
            padding-right: 12px;
        }

        .school-title {
            font-size: 27px;
        }

        .school-subtitle {
            font-size: 14px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FIND LOGO
# ============================================================

logo_candidates = [
    "assets/shs_logo.jpg.jpg",
    "assets/shs_logo.jpg",
    "assets/shs_logo.png",
    "assets/logo.jpg",
    "assets/logo.png"
]

logo_path = None

for path in logo_candidates:
    if os.path.exists(path):
        logo_path = path
        break


# ============================================================
# DISPLAY LOGO
# ============================================================

if logo_path:

    st.markdown('<div class="logo-box">', unsafe_allow_html=True)

    st.image(
        logo_path,
        width=145
    )

    st.markdown('</div>', unsafe_allow_html=True)

else:

    st.markdown(
        """
        <div class="logo-box">
            <div style="font-size:80px;">🏫</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="school-header">

        <div class="school-title">
            SHS SCHOOL CHATBOT
        </div>

        <div class="school-subtitle">
            Sacred Heart School, Moga
        </div>

        <div class="gold-line"></div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# KNOWLEDGE BASE
# ============================================================

knowledge = {

    "hello": """
👋 **Hello!**

Welcome to **Sacred Heart School, Moga**.

How can I help you today?
""",

    "school": f"""
🏫 **Sacred Heart School, Moga**

📍 Address: {ADDRESS}

👩‍🏫 Principal: {PRINCIPAL}

⏰ School Timing: {SCHOOL_TIMING}

📘 Board: {BOARD}

📚 Classes: Nursery to Class 12

📞 Phone: {PHONE}

🌐 Website: {SCHOOL_WEBSITE}
""",

    "board": f"""
📘 **Board**

Sacred Heart School, Moga follows the **{BOARD} Board**.
""",

    "board website": f"""
🌐 **ICSE / CISCE Website**

The official CISCE website is:

{CISCE_WEBSITE}
""",

    "school website": f"""
🌐 **SHS School Website**

The official school website is:

{SCHOOL_WEBSITE}
""",

    "principal": f"""
👩‍🏫 **Principal**

The Principal of Sacred Heart School, Moga is:

**{PRINCIPAL}**
""",

    "timing": f"""
⏰ **School Timing**

The school timing is:

**{SCHOOL_TIMING}**
""",

    "address": f"""
📍 **School Address**

{SCHOOL_NAME}

{ADDRESS}
""",

    "contact": f"""
☎️ **Contact SHS School**

Phone:
**{PHONE}**

📧 Principal:
{EMAIL_PRINCIPAL}

📧 Administration:
{EMAIL_ADMIN}

📧 Feedback:
{EMAIL_FEEDBACK}

📍 Address:
{ADDRESS}
""",

    "email": f"""
📧 **Email Contacts**

Principal:
{EMAIL_PRINCIPAL}

Administration:
{EMAIL_ADMIN}

Feedback:
{EMAIL_FEEDBACK}
""",

    "admission": """
📝 **Admissions**

For current admission information, please contact the school administration office.

SHS School provides education from **Nursery to Class 12**.
""",

    "fees": """
💰 **Fees**

For the latest and official fee structure, please contact the school accounts or administration office.
""",

    "library": """
📚 **Library**

Sacred Heart School has a library facility for students.

The library supports reading, learning and academic activities.
""",

    "labs": """
🔬 **Laboratories**

The school has several laboratory facilities, including:

💻 Computer Lab

⚛️ Physics Lab

🧪 Chemistry Lab

🧬 Biology Lab

📖 English Lab

📐 Mathematics Lab

🧊 3D Lab
""",

    "sports": """
🏆 **Sports Facilities**

The school provides a wide range of sports facilities:

🏏 Cricket pitch

🏏 Cricket nets

⚽ Football ground

🏀 Basketball court

🏐 Volleyball court

🏸 Badminton courts

🏃 Sports ground

And other sports facilities.
""",

    "transport": """
🚌 **Transport**

School van/transport facilities are available in nearby areas.

For specific routes and availability, please contact the school administration.
""",

    "uniform": """
👔 **School Uniform**

Students are required to wear the prescribed school uniform.

For exact information about:

• Summer uniform
• Winter uniform
• Uniform days
• Different uniform types

please check the official school instructions or contact the administration office.

📸 Uniform pictures can also be added to a future version of the chatbot.
""",

    "smart board": """
🖥️ **Smart Learning**

SHS School uses smart boards to support interactive and modern learning.

This helps teachers provide students with a more engaging learning experience.
""",

    "facilities": """
🏫 **School Facilities**

The school provides facilities including:

❄️ Air-conditioning in relevant areas

🌀 Fans

💡 Good lighting

💧 Water coolers

🚻 Clean washrooms

🖥️ Smart boards

🏆 Sports facilities

🔬 Laboratories

📚 Library
""",

    "streams": """
🎓 **Class 12 Streams**

SHS School has three Class 12 streams:

1. **NMED**
2. **SMED — Super Medical**
3. **MED — Medical**
""",

    "subjects": """
📚 **Subjects**

The school offers a broad range of subjects across different classes.

Class 12 has the following streams:

• NMED
• SMED — Super Medical
• MED — Medical

The exact subject combinations depend on the stream and class.
""",

    "exams": """
📝 **Examinations**

For current examination dates, schedules and detailed examination information, please contact the school administration/examination department.
""",

    "feedback": f"""
💬 **Feedback**

For feedback, contact:

{EMAIL_FEEDBACK}
""",

    "thank": """
😊 You're welcome!

I'm happy to help.
""",

    "bye": """
👋 Goodbye!

Have a wonderful day at SHS School!
"""
}


# ============================================================
# STUDENT LEADERS
# ============================================================

student_leaders = [

    ("Head (Boy)", "Harsahib Singh Aulakh", "XII-NMED"),

    ("Head (Girl)", "Jaismeen Kaur", "XII-SMED"),

    ("Secretary", "Ekjot Singh", "XII-SMED"),

    ("", "Ashmeet Kaur Sidhu", "XII-SMED"),

    ("Cultural Secretary", "Jobanpreet Singh", "XII-NMED"),

    ("", "Savreen Kaur Bhullar", "XII-SMED"),

    ("Sports Captain", "Varleen Kaur", "XII-MED"),

    ("Sports Vice Captain", "Jagroop Singh Dhaliwal", "XII-MED"),

    ("Sports Captain (Primary Wing)", "Ekampreet Kaur", "V-PEARL"),

    ("Sports Vice Captain (Primary Wing)", "Gurnavreet Kaur", "IV-JADE"),

    ("Club Coordinator", "Avneesh Kaur Brar", "XII-NMED"),

    ("Club Coordinator", "Ashna Pruthi", "XII-SMED"),

    ("Club Coordinator", "Manveer Singh Plaha", "XII-NMED"),

    ("Club Coordinator", "Sakhi", "XII-NMED"),

    ("Club Coordinator", "Beerkamal Kaur Gill", "XII-MED"),

    ("Club Coordinator", "Amreet Kaur Brar", "XII-NMED"),

    ("Club Coordinator", "Angel", "XII-SMED"),

    ("Club Coordinator", "Sukhman Singh Brar", "XII-NMED"),

    ("Club Coordinator", "Simaksh Gupta", "XII-NMED"),

    ("Club Coordinator", "Harjotsroop Kaur Brar", "XII-MED"),

    ("Club Coordinator", "Angel", "XII-MED"),

    ("Club Coordinator", "Parneet Kaur", "XII-MED"),

    ("Club Coordinator", "Tajveer Singh", "XII-NMED"),

    ("Club Coordinator", "Karamjeet Kaur Kalsi", "XII-MED"),

    ("Club Coordinator", "Eknoor Singh", "XII-MED"),

    ("Club Coordinator", "Manvinder Kaur", "XII-SMED"),

    ("Club Coordinator", "Jasmine Kaur", "XII-SMED"),

    ("Club Coordinator", "Upkeerat Kaur", "XII-SMED"),
]


# ============================================================
# CHATBOT FUNCTION
# ============================================================

def get_answer(message):

    user = message.lower().strip()

    # --------------------------------------------------------
    # GREETINGS
    # --------------------------------------------------------

    if any(word in user for word in [
        "hello",
        "hi",
        "hey",
        "hii",
        "hlo",
        "helo",
        "namaste"
    ]):
        return knowledge["hello"]


    # --------------------------------------------------------
    # BOARD WEBSITE
    # IMPORTANT: CHECK THIS BEFORE NORMAL BOARD
    # --------------------------------------------------------

    if (
        ("board" in user and "website" in user)
        or "cisce" in user
        or "cisce.org" in user
        or "icse website" in user
        or "board ki website" in user
        or "board website" in user
    ):
        return knowledge["board website"]


    # --------------------------------------------------------
    # SCHOOL WEBSITE
    # --------------------------------------------------------

    if (
        "school website" in user
        or "school ki website" in user
        or "shs website" in user
        or "shsmoga" in user
        or "shsmoga.com" in user
    ):
        return knowledge["school website"]


    # --------------------------------------------------------
    # BOARD
    # --------------------------------------------------------

    if any(phrase in user for phrase in [
        "board",
        "icse",
        "which board",
        "what board",
        "school board",
        "kaunsa board",
        "kaun sa board",
        "kon sa board",
        "kis board",
        "kis board par",
        "board kya hai",
        "board kaunsa"
    ]):
        return knowledge["board"]


    # --------------------------------------------------------
    # PRINCIPAL
    # --------------------------------------------------------

    if any(phrase in user for phrase in [
        "principal",
        "principal kaun",
        "principal kon",
        "principal name",
        "who is principal",
        "who is the principal",
        "principal ka naam"
    ]):
        return knowledge["principal"]


    # --------------------------------------------------------
    # TIMING
    # --------------------------------------------------------

    if any(phrase in user for phrase in [
        "timing",
        "timings",
        "school timing",
        "school timings",
        "school time",
        "school ka time",
        "school ki timing",
        "school kab",
        "kitne baje school",
        "school kitne baje",
        "school starts",
        "school start time"
    ]):
        return knowledge["timing"]


    # --------------------------------------------------------
    # ADDRESS
    # --------------------------------------------------------

    if any(phrase in user for phrase in [
        "address",
        "location",
        "school kaha",
        "school kahan",
        "school kahaan",
        "where is school",
        "where is the school"
    ]):
        return knowledge["address"]


    # --------------------------------------------------------
    # CONTACT
    # --------------------------------------------------------

    if any(phrase in user for phrase in [
        "contact",
        "phone",
        "telephone",
        "number",
        "mobile",
        "contact number"
    ]):
        return knowledge["contact"]


    # --------------------------------------------------------
    # EMAIL
    # --------------------------------------------------------

    if any(phrase in user for phrase in [
        "email",
        "e-mail",
        "mail id",
        "email id"
    ]):
        return knowledge["email"]


    # --------------------------------------------------------
    # ADMISSION
    # --------------------------------------------------------

    if "admission" in user or "admissions" in user:
        return knowledge["admission"]


    # --------------------------------------------------------
    # FEES
    # --------------------------------------------------------

    if "fee" in user or "fees" in user:
        return knowledge["fees"]


    # --------------------------------------------------------
    # LIBRARY
    # --------------------------------------------------------

    if "library" in user or "libary" in user:
        return knowledge["library"]


    # --------------------------------------------------------
    # LABS
    # --------------------------------------------------------

    if any(word in user for word in [
        "lab",
        "labs",
        "laboratory",
        "physics lab",
        "chemistry lab",
        "biology lab",
        "computer lab",
        "math lab",
        "mathematics lab",
        "english lab",
        "3d lab"
    ]):
        return knowledge["labs"]


    # --------------------------------------------------------
    # SPORTS
    # --------------------------------------------------------

    if any(word in user for word in [
        "sports",
        "sport",
        "cricket",
        "football",
        "basketball",
        "volleyball",
        "badminton",
        "sports ground",
        "sports facilities"
    ]):
        return knowledge["sports"]


    # --------------------------------------------------------
    # TRANSPORT
    # --------------------------------------------------------

    if any(word in user for word in [
        "transport",
        "bus",
        "van",
        "school bus",
        "school van"
    ]):
        return knowledge["transport"]


    # --------------------------------------------------------
    # UNIFORM
    # --------------------------------------------------------

    if any(word in user for word in [
        "uniform",
        "school dress",
        "dress",
        "summer uniform",
        "winter uniform"
    ]):
        return knowledge["uniform"]


    # --------------------------------------------------------
    # SMART BOARD
    # --------------------------------------------------------

    if any(word in user for word in [
        "smart board",
        "smartboard",
        "smart class",
        "smart study",
        "digital class"
    ]):
        return knowledge["smart board"]


    # --------------------------------------------------------
    # FACILITIES
    # --------------------------------------------------------

    if any(word in user for word in [
        "facilities",
        "facility",
        "washroom",
        "washrooms",
        "toilet",
        "water cooler",
        "drinking water",
        "fans",
        "lights",
        "ac",
        "air conditioning",
        "air conditioner"
    ]):
        return knowledge["facilities"]


    # --------------------------------------------------------
    # STREAMS
    # --------------------------------------------------------

    if any(word in user for word in [
        "stream",
        "streams",
        "nmed",
        "smed",
        "super medical",
        "medical stream",
        "class 12 stream",
        "12th stream"
    ]):
        return knowledge["streams"]


    # --------------------------------------------------------
    # SUBJECTS
    # --------------------------------------------------------

    if "subject" in user or "subjects" in user:
        return knowledge["subjects"]


    # --------------------------------------------------------
    # EXAMS
    # --------------------------------------------------------

    if any(word in user for word in [
        "exam",
        "exams",
        "examination",
        "examinations",
        "date sheet",
        "datesheet",
        "exam date"
    ]):
        return knowledge["exams"]


    # --------------------------------------------------------
    # STUDENT LEADERS
    # --------------------------------------------------------

    if any(phrase in user for phrase in [
        "student leader",
        "student leaders",
        "head boy",
        "head girl",
        "sports captain",
        "sports vice captain",
        "cultural secretary",
        "secretary",
        "club coordinator",
        "club coordinators"
    ]):

        answer = "👥 **SHS Student Leadership**\n\n"

        for designation, name, class_section in student_leaders:

            if designation:
                answer += (
                    f"• **{designation}:** "
                    f"{name} — {class_section}\n"
                )

            else:
                answer += (
                    f"• {name} — {class_section}\n"
                )

        return answer


    # --------------------------------------------------------
    # THANKS
    # --------------------------------------------------------

    if any(word in user for word in [
        "thanks",
        "thank you",
        "thankyou",
        "thx"
    ]):
        return knowledge["thank"]


    # --------------------------------------------------------
    # BYE
    # --------------------------------------------------------

    if any(word in user for word in [
        "bye",
        "goodbye",
        "good bye",
        "see you"
    ]):
        return knowledge["bye"]


    # --------------------------------------------------------
    # SCHOOL GENERAL
    # --------------------------------------------------------

    if any(word in user for word in [
        "tell me about school",
        "about school",
        "school information",
        "school info",
        "shs information",
        "shs info"
    ]):
        return knowledge["school"]


    # --------------------------------------------------------
    # UNKNOWN
    # --------------------------------------------------------

    return """
🤖 **I'm sorry, I don't have that information yet.**

You can ask me about:

🏫 School Information  
📘 ICSE Board  
🌐 School Website  
👩‍🏫 Principal  
⏰ School Timings  
📝 Admissions  
💰 Fees  
📚 Library  
🔬 Laboratories  
🏆 Sports  
🚌 Transport  
👔 Uniform  
🖥️ Smart Boards  
🎓 Streams & Subjects  
📝 Examinations  
👥 Student Leaders  
☎️ Contact Details  

You can ask in **English or Hinglish**.
"""


# ============================================================
# CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = [

        {
            "role": "assistant",
            "content": """
👋 **Hello! Welcome to SHS School Chatbot.**

I can help you with information about **Sacred Heart School, Moga**.

You can ask me questions in **English or Hinglish**.

For example:

• What is the board?

• School ka timing kya hai?

• Principal kaun hai?

• What sports are available?

• School mein kaun se labs hain?

• Class 12 mein kaun se streams hain?
"""
        }

    ]


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message(
            "user",
            avatar="👤"
        ):

            st.markdown(message["content"])

    else:

        with st.chat_message(
            "assistant",
            avatar="🏫"
        ):

            st.markdown(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

user_message = st.chat_input(
    "Ask your question in English or Hinglish..."
)


# ============================================================
# PROCESS USER MESSAGE
# ============================================================

if user_message:

    # ----------------------------------------
    # Display user message
    # ----------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.markdown(user_message)


    # ----------------------------------------
    # Bot thinking animation
    # ----------------------------------------

    with st.chat_message(
        "assistant",
        avatar="🏫"
    ):

        thinking = st.empty()

        for dots in range(1, 4):

            animated_dots = "." * dots

            thinking.markdown(
                f"""
                <div class="thinking-box">
                    🤖 SHS Bot is thinking
                    <span class="thinking-dots">
                        {animated_dots}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(0.45)


        # ------------------------------------
        # Generate answer
        # ------------------------------------

        answer = get_answer(user_message)

        thinking.empty()

        st.markdown(answer)


    # ----------------------------------------
    # Save bot response
    # ----------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
