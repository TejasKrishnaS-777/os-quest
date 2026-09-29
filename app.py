import streamlit as st
import json
import os
import random
import time

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="OS Quest",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

SAVE_FILE = "os_quest_save.json"


# =========================================================
# DARK FUTURISTIC UI
# =========================================================

st.markdown("""
<style>

/* =========================
   MAIN APP
   ========================= */

.stApp {
    background:
        radial-gradient(circle at top left, #102a43 0%, #07111f 35%, #03070d 100%);
    color: white;
}

.main {
    padding-top: 1rem;
}

h1, h2, h3 {
    color: #ffffff !important;
}

p, label, span {
    color: #e8f1ff;
}


/* =========================
   DARK SIDEBAR
   ========================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #03070d 0%,
        #050d18 45%,
        #071522 100%
    ) !important;

    border-right: 1px solid #183b56 !important;
}

section[data-testid="stSidebar"] > div {
    background: linear-gradient(
        180deg,
        #03070d 0%,
        #050d18 45%,
        #071522 100%
    ) !important;
}

/* Sidebar all text */

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #e8f1ff !important;
}


/* Sidebar profile card */

section[data-testid="stSidebar"] .card {
    background: linear-gradient(
        145deg,
        #0b1828,
        #050d17
    ) !important;

    border: 1px solid #1d405e !important;
}


/* Sidebar navigation */

section[data-testid="stSidebar"] div[data-testid="stRadio"] {
    background: transparent !important;
}

section[data-testid="stSidebar"] div[data-testid="stRadio"] > div {
    gap: 7px !important;
}

section[data-testid="stSidebar"] div[data-testid="stRadio"] label {
    background: #091625 !important;

    border: 1px solid #183b56 !important;

    border-radius: 12px !important;

    padding: 11px 14px !important;

    margin-bottom: 5px !important;

    color: #ffffff !important;

    transition: all 0.2s ease !important;
}


/* Navigation hover */

section[data-testid="stSidebar"] div[data-testid="stRadio"] label:hover {
    background: #10283d !important;

    border-color: #00f5ff !important;

    box-shadow:
        0 0 12px rgba(0,245,255,0.15) !important;
}


/* Selected navigation */

section[data-testid="stSidebar"]
div[data-testid="stRadio"]
label:has(input:checked) {

    background:
        linear-gradient(
            135deg,
            #123b59,
            #0b243a
        ) !important;

    border-color: #00f5ff !important;

    box-shadow:
        0 0 15px rgba(0,245,255,0.2) !important;
}


/* Navigation text */

section[data-testid="stSidebar"]
div[data-testid="stRadio"]
label p {

    color: #ffffff !important;

    font-weight: 700 !important;

    font-size: 14px !important;
}


/* Sidebar buttons */

section[data-testid="stSidebar"] .stButton > button {

    background:
        linear-gradient(
            135deg,
            #0a1726,
            #07111d
        ) !important;

    color: #ffffff !important;

    border: 1px solid #183b56 !important;

    border-radius: 10px !important;
}


/* Sidebar button hover */

section[data-testid="stSidebar"] .stButton > button:hover {

    background: #10283d !important;

    color: #00f5ff !important;

    border-color: #00f5ff !important;

    box-shadow:
        0 0 12px rgba(0,245,255,0.15) !important;
}


/* Sidebar divider */

section[data-testid="stSidebar"] hr {
    border-color: #183b56 !important;
}


/* =========================
   HERO
   ========================= */

.hero {

    background:
        linear-gradient(
            135deg,
            #0b1d33,
            #07101d
        );

    border: 1px solid #1f496d;

    border-radius: 22px;

    padding: 30px;

    margin-bottom: 25px;

    box-shadow:
        0 0 30px rgba(0,220,255,0.10);
}

.hero-title {

    font-size: 42px;

    font-weight: 900;

    color: #00f5ff;

    text-shadow:
        0 0 15px rgba(0,245,255,0.5);
}

.hero-subtitle {

    font-size: 20px;

    color: #b8d8f5;

    margin-top: 5px;
}


/* =========================
   CARDS
   ========================= */

.card {

    background:
        linear-gradient(
            145deg,
            #0c1b2e,
            #07111f
        );

    border: 1px solid #1d405e;

    border-radius: 18px;

    padding: 22px;

    margin: 10px 0;

    box-shadow:
        0 0 18px rgba(0,180,255,0.06);
}


/* =========================
   QUEST CARDS
   ========================= */

.quest-card {

    background:
        linear-gradient(
            145deg,
            #10243b,
            #081321
        );

    border: 1px solid #285476;

    border-radius: 18px;

    padding: 20px;

    min-height: 180px;

    margin-bottom: 15px;
}

.locked {
    opacity: 0.55;
}


/* =========================
   STAT BOXES
   ========================= */

.stat-box {

    background:
        linear-gradient(
            145deg,
            #0e2137,
            #081321
        );

    border: 1px solid #214a6a;

    border-radius: 16px;

    padding: 18px;

    text-align: center;
}

.stat-number {

    font-size: 30px;

    font-weight: 900;

    color: #00f5ff;
}

.stat-label {

    color: #9dbbd5;

    font-size: 14px;
}


/* =========================
   XP BOX
   ========================= */

.xp-box {

    background:
        linear-gradient(
            135deg,
            #20183d,
            #0c1730
        );

    border: 1px solid #654cb5;

    border-radius: 16px;

    padding: 20px;

    text-align: center;
}


/* =========================
   BADGES
   ========================= */

.badge {

    display: inline-block;

    background:
        linear-gradient(
            135deg,
            #132b45,
            #0b1626
        );

    border: 1px solid #316386;

    border-radius: 14px;

    padding: 12px 16px;

    margin: 5px;

    font-weight: bold;
}


/* =========================
   SPEED ROUND
   ========================= */

.speed-box {

    background:
        linear-gradient(
            135deg,
            #291638,
            #111329
        );

    border: 2px solid #a44cff;

    border-radius: 20px;

    padding: 25px;

    text-align: center;

    box-shadow:
        0 0 25px rgba(164,76,255,0.18);
}

.timer {

    font-size: 42px;

    font-weight: 900;

    color: #ffcc00;
}


/* =========================
   CERTIFICATE
   ========================= */

.certificate {

    background:
        linear-gradient(
            145deg,
            #101f35,
            #07101c
        );

    border: 3px solid #00f5ff;

    border-radius: 25px;

    padding: 45px;

    text-align: center;

    box-shadow:
        0 0 35px rgba(0,245,255,0.2);
}

.certificate-title {

    font-size: 38px;

    font-weight: 900;

    color: #00f5ff;
}


/* =========================
   QUIZ OPTIONS
   ========================= */

div[data-testid="stRadio"] > div {
    gap: 10px;
}

div[data-testid="stRadio"] label,
div[role="radiogroup"] label {

    background:
        linear-gradient(
            145deg,
            #101d32,
            #0a1222
        ) !important;

    border: 1px solid #315274 !important;

    border-radius: 12px !important;

    padding: 12px 16px !important;

    margin-bottom: 8px !important;

    color: #ffffff !important;

    cursor: pointer !important;

    transition: 0.2s !important;
}

div[data-testid="stRadio"] label:hover,
div[role="radiogroup"] label:hover {

    border-color: #00f5ff !important;

    background:
        linear-gradient(
            145deg,
            #132943,
            #0d1a2d
        ) !important;

    box-shadow:
        0 0 12px rgba(0,245,255,0.18) !important;
}

div[data-testid="stRadio"] label p,
div[role="radiogroup"] label p {

    color: #ffffff !important;

    font-size: 15px !important;

    font-weight: 600 !important;
}

div[data-testid="stRadio"] label span,
div[role="radiogroup"] label span {

    color: #ffffff !important;
}

div[data-testid="stRadio"] label:has(input:checked),
div[role="radiogroup"] label:has(input:checked) {

    border-color: #00f5ff !important;

    background:
        linear-gradient(
            145deg,
            #12304a,
            #0d1c30
        ) !important;

    box-shadow:
        0 0 15px rgba(0,245,255,0.2) !important;
}

div[data-testid="stRadio"] input,
div[role="radiogroup"] input {

    accent-color: #00f5ff !important;
}


/* =========================
   BUTTONS
   ========================= */

button {
    border-radius: 10px !important;
}

.stButton > button {

    background:
        linear-gradient(
            135deg,
            #123b59,
            #0b243a
        );

    color: white;

    border: 1px solid #286080;

    font-weight: bold;

    transition: 0.2s;
}

.stButton > button:hover {

    border-color: #00f5ff;

    color: #00f5ff;

    box-shadow:
        0 0 15px rgba(0,245,255,0.2);
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# DEFAULT GAME DATA
# =========================================================

def get_defaults():

    return {

        "page": "home",

        "player_name": "",

        "profile_created": False,

        "xp": 0,

        "level1_completed": False,
        "level2_completed": False,
        "level3_completed": False,
        "level4_completed": False,

        "process_state": "NEW",

        "process_challenge_done": False,
        "fcfs_challenge_done": False,
        "memory_challenge_done": False,
        "page_challenge_done": False,

        "quiz_index": {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0
        },

        "quiz_completed": {
            "1": False,
            "2": False,
            "3": False,
            "4": False
        },

        "quiz_scores": {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0
        },

        "lives": {
            "1": 3,
            "2": 3,
            "3": 3,
            "4": 3
        },

        "streak": 0,

        "best_streak": 0,

        "badges": [],

        "total_attempts": 0,

        "wrong_answers": 0,

        "correct_answers": 0,

        "speed_round_score": 0,

        "speed_round_completed": False,

        "game_started": False
    }


# =========================================================
# SAVE / LOAD
# =========================================================

def save_progress():

    data = {}

    for key, value in st.session_state.items():

        if key.startswith("_"):
            continue

        try:

            json.dumps(value)

            data[key] = value

        except:

            pass

    with open(
        SAVE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def load_progress():

    defaults = get_defaults()

    if os.path.exists(SAVE_FILE):

        try:

            with open(
                SAVE_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                saved = json.load(file)

            defaults.update(saved)

        except:

            pass

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


if "loaded" not in st.session_state:

    load_progress()

    st.session_state.loaded = True


# =========================================================
# GAME FUNCTIONS
# =========================================================

def save_game():

    save_progress()


def add_xp(amount):

    st.session_state.xp += amount

    save_game()


def completed_levels():

    total = 0

    for i in range(1, 5):

        if st.session_state[f"level{i}_completed"]:

            total += 1

    return total


def level_unlocked(level):

    if level == 1:

        return True

    return st.session_state[
        f"level{level - 1}_completed"
    ]


def unlock_badge(name):

    if name not in st.session_state.badges:

        st.session_state.badges.append(name)

        save_game()


def level_complete(level):

    st.session_state[
        f"level{level}_completed"
    ] = True

    if level == 1:

        unlock_badge("⚙️ PROCESS MASTER")

    elif level == 2:

        unlock_badge("🧠 CPU MASTER")

    elif level == 3:

        unlock_badge("💾 MEMORY MASTER")

    elif level == 4:

        unlock_badge("📄 PAGE MASTER")

        unlock_badge("🏆 OS MASTER")

    save_game()


def reset_streak():

    st.session_state.streak = 0


def update_streak():

    st.session_state.streak += 1

    if st.session_state.streak > st.session_state.best_streak:

        st.session_state.best_streak = \
            st.session_state.streak

    if st.session_state.streak == 2:

        add_xp(10)

    elif st.session_state.streak == 3:

        add_xp(20)

    elif st.session_state.streak >= 4:

        add_xp(30)

        unlock_badge("🔥 STREAK MASTER")


def lives_display(level):

    lives = st.session_state.lives[str(level)]

    return (
        "❤️" * lives +
        "🖤" * (3 - lives)
    )


def reset_game():

    if os.path.exists(SAVE_FILE):

        os.remove(SAVE_FILE)

    for key in list(st.session_state.keys()):

        del st.session_state[key]

    st.rerun()


# =========================================================
# QUIZ FUNCTION
# =========================================================

def run_quiz(level, questions):

    key = str(level)

    index = st.session_state.quiz_index[key]

    if index >= len(questions):

        if not st.session_state.quiz_completed[key]:

            st.session_state.quiz_completed[key] = True

            level_complete(level)

            add_xp(50)

            unlock_badge("🎯 QUIZ PLAYER")

            st.success(
                "🎉 Quiz completed! +50 XP"
            )

            save_game()

        return

    question = questions[index]

    st.markdown("---")

    st.markdown(
        f"""
        <div class="card">

        <h2>🧠 Quest Quiz</h2>

        <h3>
        Question {index + 1} / {len(questions)}
        </h3>

        <p>
        {question["question"]}
        </p>

        <p>
        ❤️ Lives: {lives_display(level)}
        </p>

        <p>
        🔥 Current Streak:
        {st.session_state.streak}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    answer = st.radio(
        "Choose your answer:",
        question["options"],
        key=f"quiz_{level}_{index}"
    )

    if st.button(
        "⚡ SUBMIT ANSWER",
        key=f"submit_{level}_{index}"
    ):

        st.session_state.total_attempts += 1

        if answer == question["answer"]:

            st.session_state.correct_answers += 1

            st.session_state.quiz_scores[key] += 1

            st.session_state.quiz_index[key] += 1

            update_streak()

            add_xp(20)

            unlock_badge("🧠 FIRST QUIZ")

            st.success(
                "✅ Correct! +20 XP"
            )

        else:

            st.session_state.wrong_answers += 1

            st.session_state.lives[key] -= 1

            reset_streak()

            if st.session_state.lives[key] <= 0:

                st.session_state.lives[key] = 3

                st.session_state.quiz_index[key] = 0

                st.error(
                    "💀 All lives lost! "
                    "Quiz restarted."
                )

            else:

                st.error(
                    f"❌ Wrong! Correct answer: "
                    f"{question['answer']}"
                )

        save_game()

        st.rerun()


# =========================================================
# PLAYER SETUP
# =========================================================

if not st.session_state.profile_created:

    st.markdown(
        """
        <div class="hero">

            <div class="hero-title">
                ⚙️ OS QUEST
            </div>

            <div class="hero-subtitle">
                THE OPERATING SYSTEM ADVENTURE
            </div>

            <br>

            <p>
                Learn Operating Systems through
                quests, challenges, XP, lives,
                streaks and achievements.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 👤 Create Your Player")

    name = st.text_input(
        "Enter your player name",
        placeholder="Example: Tejas"
    )

    if st.button("🚀 START QUEST"):

        if name.strip():

            st.session_state.player_name = \
                name.strip()

            st.session_state.profile_created = True

            st.session_state.game_started = True

            unlock_badge("🎮 QUEST BEGINNER")

            save_game()

            st.rerun()

        else:

            st.warning(
                "Please enter your name."
            )

    st.stop()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ⚙️ OS QUEST")

    st.markdown(
        f"""
        <div class="card">

        👤 <b>
        {st.session_state.player_name}
        </b>

        <br><br>

        ⭐ XP:
        <b>{st.session_state.xp}</b>

        <br>

        🏆 Quests:
        <b>{completed_levels()}/4</b>

        <br>

        🔥 Best Streak:
        <b>{st.session_state.best_streak}</b>

        </div>
        """,
        unsafe_allow_html=True
    )

    menu = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "📚 Learn",
            "⚡ Speed Round",
            "📊 Report"
        ]
    )

    st.markdown("---")

    if st.button(
        "💾 Save Game",
        use_container_width=True
    ):

        save_game()

        st.success("Game saved!")

    if st.button(
        "🔄 New Game",
        use_container_width=True
    ):

        reset_game()


# =========================================================
# HOME
# =========================================================

if menu == "🏠 Home":

    st.markdown(
        f"""
        <div class="hero">

            <div class="hero-title">
                ⚙️ OS QUEST
            </div>

            <div class="hero-subtitle">
                THE OPERATING SYSTEM ADVENTURE
            </div>

            <br>

            <h3>
            Welcome,
            {st.session_state.player_name}! 👋
            </h3>

            <p>
            Ready to master Operating Systems?
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            f"""
            <div class="stat-box">

            <div class="stat-number">
            {st.session_state.xp}
            </div>

            <div class="stat-label">
            TOTAL XP
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="stat-box">

            <div class="stat-number">
            {completed_levels()}/4
            </div>

            <div class="stat-label">
            QUESTS COMPLETE
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="stat-box">

            <div class="stat-number">
            {st.session_state.best_streak}
            </div>

            <div class="stat-label">
            BEST STREAK
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:

        if st.session_state.total_attempts > 0:

            accuracy = int(
                st.session_state.correct_answers /
                st.session_state.total_attempts *
                100
            )

        else:

            accuracy = 0

        st.markdown(
            f"""
            <div class="stat-box">

            <div class="stat-number">
            {accuracy}%
            </div>

            <div class="stat-label">
            ACCURACY
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("📈 Overall Progress")

    st.progress(
        completed_levels() / 4
    )

    st.write(
        f"{completed_levels()} of 4 quests completed"
    )

    st.markdown("## 🗺️ QUEST MAP")

    quests = [

        (
            1,
            "⚙️ Process Management",
            "Learn process states and lifecycle."
        ),

        (
            2,
            "🧠 CPU Scheduling",
            "Master FCFS scheduling."
        ),

        (
            3,
            "💾 Memory Management",
            "Learn First Fit allocation."
        ),

        (
            4,
            "📄 Page Replacement",
            "Understand FIFO and LRU."
        )
    ]

    for level, title, description in quests:

        unlocked = level_unlocked(level)

        completed = \
            st.session_state[
                f"level{level}_completed"
            ]

        if completed:

            status = "✅ COMPLETED"

        elif unlocked:

            status = "🔓 UNLOCKED"

        else:

            status = "🔒 LOCKED"

        css = "" if unlocked else "locked"

        st.markdown(
            f"""
            <div class="quest-card {css}">

            <h2>{title}</h2>

            <p>{description}</p>

            <br>

            <b>{status}</b>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("## 🏅 ACHIEVEMENTS")

    if st.session_state.badges:

        for badge in st.session_state.badges:

            st.markdown(
                f"""
                <span class="badge">
                {badge}
                </span>
                """,
                unsafe_allow_html=True
            )

    else:

        st.info(
            "Complete quests to unlock badges!"
        )

    st.markdown("---")

    st.info(
        "💡 Tip: Build a streak by answering "
        "questions correctly."
    )


# =========================================================
# LEARN
# =========================================================

elif menu == "📚 Learn":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-title">
                📚 OS QUESTS
            </div>

            <div class="hero-subtitle">
                Complete each quest to unlock the next one.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    level = st.selectbox(
        "Choose Quest",
        [1, 2, 3, 4],
        format_func=lambda x: {
            1: "⚙️ Level 1 - Process Management",
            2: "🧠 Level 2 - CPU Scheduling",
            3: "💾 Level 3 - Memory Management",
            4: "📄 Level 4 - Page Replacement"
        }[x]
    )

    if not level_unlocked(level):

        st.error(
            f"🔒 Level {level} is locked. "
            f"Complete Level {level-1} first."
        )

        st.stop()


    # =====================================================
    # LEVEL 1
    # =====================================================

    if level == 1:

        st.markdown(
            "## ⚙️ Level 1: Process Management"
        )

        st.markdown(
            """
            <div class="card">

            <h2>What is a Process?</h2>

            <p>
            A process is a program that is
            currently being executed.
            </p>

            <h3>Process States</h3>

            <ul>
                <li>🆕 NEW - Process is being created</li>
                <li>🟡 READY - Waiting for CPU</li>
                <li>🟢 RUNNING - Using CPU</li>
                <li>🟠 WAITING - Waiting for an event</li>
                <li>🔴 TERMINATED - Execution finished</li>
            </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            "### 🎮 Process Lifecycle Simulator"
        )

        current = \
            st.session_state.process_state

        st.markdown(
            f"""
            <div class="speed-box">

            <h2>Current State</h2>

            <div class="timer">
            {current}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        if current == "NEW":

            if st.button(
                "➡️ Move to READY"
            ):

                st.session_state.process_state = \
                    "READY"

                add_xp(10)

                st.rerun()

        elif current == "READY":

            if st.button(
                "➡️ Move to RUNNING"
            ):

                st.session_state.process_state = \
                    "RUNNING"

                add_xp(10)

                st.rerun()

        elif current == "RUNNING":

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "➡️ Move to WAITING"
                ):

                    st.session_state.process_state = \
                        "WAITING"

                    add_xp(10)

                    st.rerun()

            with col2:

                if st.button(
                    "🏁 Terminate"
                ):

                    st.session_state.process_state = \
                        "TERMINATED"

                    add_xp(10)

                    st.rerun()

        elif current == "WAITING":

            if st.button(
                "➡️ Back to READY"
            ):

                st.session_state.process_state = \
                    "READY"

                add_xp(10)

                st.rerun()

        elif current == "TERMINATED":

            st.success(
                "Process has completed execution."
            )

        st.markdown("---")

        st.subheader(
            "🎯 Process Challenge"
        )

        if current == "RUNNING":

            if not st.session_state.process_challenge_done:

                if st.button(
                    "🏆 COMPLETE PROCESS CHALLENGE"
                ):

                    st.session_state.process_challenge_done = True

                    add_xp(50)

                    unlock_badge(
                        "⚙️ PROCESS MASTER"
                    )

                    st.success(
                        "🎉 Challenge complete! +50 XP"
                    )

                    st.rerun()

            else:

                st.success(
                    "✅ Process Challenge Completed!"
                )

        else:

            st.info(
                "Reach RUNNING to complete "
                "the challenge."
            )

        questions = [

            {
                "question":
                "Which process state means "
                "the process is currently "
                "using the CPU?",

                "options": [
                    "READY",
                    "RUNNING",
                    "WAITING",
                    "NEW"
                ],

                "answer":
                "RUNNING"
            },

            {
                "question":
                "Which state means the process "
                "is waiting for CPU allocation?",

                "options": [
                    "READY",
                    "RUNNING",
                    "TERMINATED",
                    "NEW"
                ],

                "answer":
                "READY"
            },

            {
                "question":
                "Which state means the process "
                "has finished execution?",

                "options": [
                    "WAITING",
                    "READY",
                    "TERMINATED",
                    "RUNNING"
                ],

                "answer":
                "TERMINATED"
            },

            {
                "question":
                "A process is best described as:",

                "options": [
                    "A program in execution",
                    "A computer file",
                    "A CPU register",
                    "A memory block"
                ],

                "answer":
                "A program in execution"
            }
        ]

        run_quiz(
            1,
            questions
        )


    # =====================================================
    # LEVEL 2
    # =====================================================

    elif level == 2:

        st.markdown(
            "## 🧠 Level 2: CPU Scheduling"
        )

        st.markdown(
            """
            <div class="card">

            <h2>FCFS - First Come First Serve</h2>

            <p>
            FCFS schedules processes according
            to their arrival order.
            </p>

            <h3>Example</h3>

            <p>
            P1 = 5 ms<br>
            P2 = 3 ms<br>
            P3 = 6 ms
            </p>

            <h3>Gantt Chart</h3>

            <p>
            P1: 0 → 5<br>
            P2: 5 → 8<br>
            P3: 8 → 14
            </p>

            <h3>Waiting Time</h3>

            <p>
            P1 = 0 ms<br>
            P2 = 5 ms<br>
            P3 = 8 ms
            </p>

            <b>
            Average Waiting Time = 4.33 ms
            </b>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader(
            "🎯 FCFS Challenge"
        )

        p3_answer = st.number_input(
            "P3 Waiting Time (ms)",
            min_value=0,
            max_value=100,
            value=0
        )

        if not st.session_state.fcfs_challenge_done:

            if st.button(
                "🏆 CHECK FCFS CHALLENGE"
            ):

                if p3_answer == 8:

                    st.session_state.fcfs_challenge_done = True

                    add_xp(50)

                    st.success(
                        "🎉 Correct! +50 XP"
                    )

                    st.rerun()

                else:

                    st.error(
                        "❌ Incorrect. Try again."
                    )

        else:

            st.success(
                "✅ FCFS Challenge Completed!"
            )

        questions = [

            {
                "question":
                "FCFS stands for:",

                "options": [
                    "First Come First Serve",
                    "Fast CPU First System",
                    "First Computer File System",
                    "Fast Come Fast Serve"
                ],

                "answer":
                "First Come First Serve"
            },

            {
                "question":
                "FCFS is generally:",

                "options": [
                    "Preemptive",
                    "Non-preemptive",
                    "Random",
                    "Priority based"
                ],

                "answer":
                "Non-preemptive"
            },

            {
                "question":
                "If P1 arrives first, which "
                "process gets CPU first?",

                "options": [
                    "P3",
                    "P2",
                    "P1",
                    "None"
                ],

                "answer":
                "P1"
            },

            {
                "question":
                "What is the waiting time "
                "of P3?",

                "options": [
                    "5 ms",
                    "6 ms",
                    "8 ms",
                    "14 ms"
                ],

                "answer":
                "8 ms"
            }
        ]

        run_quiz(
            2,
            questions
        )


    # =====================================================
    # LEVEL 3
    # =====================================================

    elif level == 3:

        st.markdown(
            "## 💾 Level 3: Memory Management"
        )

        st.markdown(
            """
            <div class="card">

            <h2>First Fit</h2>

            <p>
            First Fit allocates a process to
            the first available memory block
            that is large enough.
            </p>

            <h3>Memory Blocks</h3>

            <p>
            Block 1 = 100 KB<br>
            Block 2 = 50 KB<br>
            Block 3 = 200 KB<br>
            Block 4 = 120 KB
            </p>

            <h3>Processes</h3>

            <p>
            P1 = 90 KB<br>
            P2 = 200 KB<br>
            P3 = 120 KB
            </p>

            <h3>Allocation</h3>

            <p>
            P1 → Block 1<br>
            P2 → Block 3<br>
            P3 → Block 4
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader(
            "🎯 Memory Allocation Challenge"
        )

        memory_answer = st.selectbox(
            "Where should P1 (90 KB) be allocated?",

            [
                "Select an option",
                "Block 1",
                "Block 2",
                "Block 3",
                "Block 4"
            ]
        )

        if not st.session_state.memory_challenge_done:

            if st.button(
                "🏆 CHECK MEMORY CHALLENGE"
            ):

                if memory_answer == "Block 1":

                    st.session_state.memory_challenge_done = True

                    add_xp(50)

                    st.success(
                        "🎉 Correct! +50 XP"
                    )

                    st.rerun()

                else:

                    st.error(
                        "❌ Incorrect. Try again."
                    )

        else:

            st.success(
                "✅ Memory Challenge Completed!"
            )

        questions = [

            {
                "question":
                "What does First Fit do?",

                "options": [
                    "Uses the first suitable memory block",
                    "Uses the largest memory block",
                    "Uses the smallest memory block",
                    "Uses a random block"
                ],

                "answer":
                "Uses the first suitable memory block"
            },

            {
                "question":
                "Where is P1 (90 KB) allocated?",

                "options": [
                    "Block 1",
                    "Block 2",
                    "Block 3",
                    "Block 4"
                ],

                "answer":
                "Block 1"
            },

            {
                "question":
                "Which block has 200 KB?",

                "options": [
                    "Block 1",
                    "Block 2",
                    "Block 3",
                    "Block 4"
                ],

                "answer":
                "Block 3"
            },

            {
                "question":
                "Which block remains free?",

                "options": [
                    "Block 1",
                    "Block 2",
                    "Block 3",
                    "Block 4"
                ],

                "answer":
                "Block 2"
            }
        ]

        run_quiz(
            3,
            questions
        )


    # =====================================================
    # LEVEL 4
    # =====================================================

    elif level == 4:

        st.markdown(
            "## 📄 Level 4: Page Replacement"
        )

        st.markdown(
            """
            <div class="card">

            <h2>Page Replacement</h2>

            <p>
            Page replacement algorithms decide
            which page should be removed when
            a new page needs to enter memory.
            </p>

            <h3>Reference String</h3>

            <p>
            1 → 2 → 3 → 1 → 4 → 2
            </p>

            <h3>Frames = 3</h3>

            <h3>FIFO</h3>

            <p>
            Removes the page that entered memory first.
            </p>

            <h3>LRU</h3>

            <p>
            Removes the page that has been unused
            for the longest time.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader(
            "🎯 Page Replacement Challenge"
        )

        page_choice = st.radio(
            "Which algorithm removes the "
            "page that entered memory first?",

            [
                "FIFO",
                "LRU",
                "FCFS",
                "First Fit"
            ]
        )

        if not st.session_state.page_challenge_done:

            if st.button(
                "🏆 CHECK PAGE CHALLENGE"
            ):

                if page_choice == "FIFO":

                    st.session_state.page_challenge_done = True

                    add_xp(50)

                    st.success(
                        "🎉 Correct! +50 XP"
                    )

                    st.rerun()

                else:

                    st.error(
                        "❌ Incorrect. Try again."
                    )

        else:

            st.success(
                "✅ Page Replacement Challenge Completed!"
            )

        questions = [

            {
                "question":
                "FIFO stands for:",

                "options": [
                    "First In First Out",
                    "Fast In Fast Out",
                    "First Input First Output",
                    "File In File Out"
                ],

                "answer":
                "First In First Out"
            },

            {
                "question":
                "Which page does FIFO remove?",

                "options": [
                    "Newest page",
                    "Oldest page",
                    "Largest page",
                    "Smallest page"
                ],

                "answer":
                "Oldest page"
            },

            {
                "question":
                "LRU stands for:",

                "options": [
                    "Least Recently Used",
                    "Last Recently Used",
                    "Least Random Usage",
                    "Latest Removed Unit"
                ],

                "answer":
                "Least Recently Used"
            },

            {
                "question":
                "How many frames are used?",

                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],

                "answer":
                "3"
            }
        ]

        run_quiz(
            4,
            questions
        )


# =========================================================
# SPEED ROUND
# =========================================================

elif menu == "⚡ Speed Round":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-title">
                ⚡ SPEED ROUND
            </div>

            <div class="hero-subtitle">
                Test your OS knowledge against the clock!
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "Answer 5 questions. "
        "You have 20 seconds for each question."
    )

    speed_questions = [

        {
            "question":
            "Which state means a process "
            "is using the CPU?",

            "options": [
                "READY",
                "RUNNING",
                "WAITING",
                "NEW"
            ],

            "answer":
            "RUNNING"
        },

        {
            "question":
            "FCFS stands for:",

            "options": [
                "First Come First Serve",
                "Fast CPU First System",
                "First Computer File System",
                "Fast Come Fast Serve"
            ],

            "answer":
            "First Come First Serve"
        },

        {
            "question":
            "Which algorithm allocates "
            "the first suitable memory block?",

            "options": [
                "FIFO",
                "LRU",
                "First Fit",
                "FCFS"
            ],

            "answer":
            "First Fit"
        },

        {
            "question":
            "Which algorithm removes "
            "the oldest page?",

            "options": [
                "LRU",
                "FIFO",
                "First Fit",
                "FCFS"
            ],

            "answer":
            "FIFO"
        },

        {
            "question":
            "What does LRU mean?",

            "options": [
                "Least Recently Used",
                "Last Recently Used",
                "Least Random Usage",
                "Latest Removed Unit"
            ],

            "answer":
            "Least Recently Used"
        },

        {
            "question":
            "Which process state waits "
            "for CPU allocation?",

            "options": [
                "READY",
                "RUNNING",
                "TERMINATED",
                "WAITING"
            ],

            "answer":
            "READY"
        },

        {
            "question":
            "What is P3 waiting time?",

            "options": [
                "0 ms",
                "5 ms",
                "8 ms",
                "14 ms"
            ],

            "answer":
            "8 ms"
        },

        {
            "question":
            "How many frames are used?",

            "options": [
                "1",
                "2",
                "3",
                "4"
            ],

            "answer":
            "3"
        }
    ]

    if "speed_questions" not in st.session_state:

        st.session_state.speed_questions = \
            random.sample(
                speed_questions,
                5
            )

        st.session_state.speed_index = 0

        st.session_state.speed_score = 0

        st.session_state.speed_started = False

        st.session_state.speed_start_time = 0

    if not st.session_state.speed_started:

        st.markdown(
            """
            <div class="speed-box">

            <h1>⚡ READY PLAYER?</h1>

            <p>5 questions</p>

            <p>20 seconds per question</p>

            <p>
            +50 XP for completing
            the round
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "🚀 START SPEED ROUND"
        ):

            st.session_state.speed_started = True

            st.session_state.speed_start_time = \
                time.time()

            st.rerun()

    else:

        index = \
            st.session_state.speed_index

        if index < 5:

            question = \
                st.session_state.speed_questions[index]

            elapsed = \
                time.time() - \
                st.session_state.speed_start_time

            remaining = max(
                0,
                20 - int(elapsed)
            )

            st.markdown(
                f"""
                <div class="speed-box">

                <h2>⚡ SPEED ROUND</h2>

                <h3>
                Question {index + 1} / 5
                </h3>

                <div class="timer">
                ⏱️ {remaining}s
                </div>

                <p>
                Score:
                {st.session_state.speed_score}
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            answer = st.radio(
                "Choose your answer:",
                question["options"],
                key=f"speed_{index}"
            )

            if remaining <= 0:

                st.error(
                    "⏰ Time's up!"
                )

                st.session_state.speed_index += 1

                st.session_state.speed_start_time = \
                    time.time()

                st.rerun()

            if st.button(
                "⚡ LOCK ANSWER"
            ):

                if answer == question["answer"]:

                    st.session_state.speed_score += 1

                    st.success(
                        "✅ Correct!"
                    )

                else:

                    st.error(
                        f"❌ Wrong! "
                        f"Correct answer: "
                        f"{question['answer']}"
                    )

                st.session_state.speed_index += 1

                st.session_state.speed_start_time = \
                    time.time()

                time.sleep(0.5)

                st.rerun()

            time.sleep(1)

            st.rerun()

        else:

            score = \
                st.session_state.speed_score

            st.markdown(
                f"""
                <div class="certificate">

                <div class="certificate-title">
                ⚡ SPEED ROUND COMPLETE
                </div>

                <h2>
                {st.session_state.player_name}
                </h2>

                <h1>
                🎯 {score} / 5
                </h1>

                <p>
                You completed the Speed Round!
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            if not st.session_state.speed_round_completed:

                st.session_state.speed_round_completed = True

                st.session_state.speed_round_score = score

                add_xp(50)

                if score == 5:

                    unlock_badge(
                        "⚡ SPEED DEMON"
                    )

                elif score >= 3:

                    unlock_badge(
                        "⚡ SPEED RUNNER"
                    )

                st.success(
                    "🏆 Speed Round reward: +50 XP"
                )

                save_game()

            if st.button(
                "🔄 PLAY SPEED ROUND AGAIN"
            ):

                st.session_state.speed_questions = \
                    random.sample(
                        speed_questions,
                        5
                    )

                st.session_state.speed_index = 0

                st.session_state.speed_score = 0

                st.session_state.speed_started = False

                st.session_state.speed_start_time = 0

                st.rerun()


# =========================================================
# REPORT
# =========================================================

elif menu == "📊 Report":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-title">
                📊 PLAYER REPORT
            </div>

            <div class="hero-subtitle">
                Your OS Quest performance
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    attempts = \
        st.session_state.total_attempts

    correct = \
        st.session_state.correct_answers

    if attempts > 0:

        accuracy = int(
            correct / attempts * 100
        )

    else:

        accuracy = 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "⭐ XP",
            st.session_state.xp
        )

    with col2:

        st.metric(
            "🏆 Quests",
            f"{completed_levels()}/4"
        )

    with col3:

        st.metric(
            "🎯 Accuracy",
            f"{accuracy}%"
        )

    with col4:

        st.metric(
            "🔥 Best Streak",
            st.session_state.best_streak
        )

    st.markdown("---")

    st.subheader(
        "📚 Quest Progress"
    )

    for i in range(1, 5):

        if st.session_state[
            f"level{i}_completed"
        ]:

            st.success(
                f"Level {i} - ✅ Completed"
            )

        elif level_unlocked(i):

            st.info(
                f"Level {i} - 🔓 Unlocked"
            )

        else:

            st.warning(
                f"Level {i} - 🔒 Locked"
            )

    st.markdown("---")

    st.subheader(
        "🧠 Quiz Performance"
    )

    names = {

        "1":
        "⚙️ Process Management",

        "2":
        "🧠 CPU Scheduling",

        "3":
        "💾 Memory Management",

        "4":
        "📄 Page Replacement"
    }

    for key, name in names.items():

        score = \
            st.session_state.quiz_scores[key]

        st.write(
            f"{name}: **{score}/4**"
        )

        st.progress(
            score / 4
        )

    st.markdown("---")

    st.subheader(
        "⚡ Speed Round"
    )

    if st.session_state.speed_round_completed:

        st.success(
            f"Best score: "
            f"{st.session_state.speed_round_score}/5"
        )

    else:

        st.info(
            "Speed Round not completed yet."
        )

    st.markdown("---")

    st.subheader(
        "🏅 Achievements"
    )

    for badge in st.session_state.badges:

        st.markdown(
            f"""
            <span class="badge">
            {badge}
            </span>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# FINAL COMPLETION
# =========================================================

if completed_levels() == 4:

    st.markdown("---")

    attempts = \
        st.session_state.total_attempts

    if attempts > 0:

        final_accuracy = int(
            st.session_state.correct_answers /
            attempts * 100
        )

    else:

        final_accuracy = 0

    st.markdown(
        f"""
        <div class="certificate">

        <div class="certificate-title">
        🏆 OS QUEST COMPLETE 🏆
        </div>

        <h2>
        {st.session_state.player_name}
        </h2>

        <p>
        has successfully completed
        all four OS quests.
        </p>

        <h3>
        ⚙️ Processes
        • 🧠 CPU Scheduling
        • 💾 Memory
        • 📄 Page Replacement
        </h3>

        <h1>
        ⭐ {st.session_state.xp} XP ⭐
        </h1>

        <p>
        🔥 Best Streak:
        {st.session_state.best_streak}
        </p>

        <p>
        🎯 Accuracy:
        {final_accuracy}%
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#7894ad;
        padding:15px;
    ">

        ⚙️ OS QUEST
        <br>

        Operating Systems Learning Game

        <br><br>

        Learn • Play • Complete • Master

    </div>
    """,
    unsafe_allow_html=True
)