"""
SpamGuard AI - Email Spam Detection
Streamlit frontend

This replaces the old HTML/CSS/JS + Flask frontend. It loads the trained
model (backend/model.pkl) directly - no separate API server needed.

Run:
    streamlit run app.py
"""

import json
from pathlib import Path

import joblib
import streamlit as st

# ----------------------------------------------------------------------
# Paths / constants
# ----------------------------------------------------------------------
BASE = Path(__file__).parent
BACKEND_DIR = (BASE.parent / "backend").resolve()
MODEL_PATH = BACKEND_DIR / "model.pkl"
METRICS_PATH = BACKEND_DIR / "metrics.json"

MIN_CHARS = 5
MAX_CHARS = 20_000

st.set_page_config(
    page_title="SpamGuard AI | Email Spam Detection",
    page_icon="🛡️",
    layout="centered",
)


# ----------------------------------------------------------------------
# Load model (cached so it only loads once per session, not per click)
# ----------------------------------------------------------------------
@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        return None
    return joblib.load(MODEL_PATH)


@st.cache_data
def load_metrics():
    if not METRICS_PATH.exists():
        return None
    return json.loads(METRICS_PATH.read_text())


model = load_model()
metrics = load_metrics()

if "history" not in st.session_state:
    st.session_state.history = []   # list of (label, confidence) for this session


# ----------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------
st.markdown(
    """
    <div style="text-align:center; padding: 0.5rem 0 1rem 0;">
        <span style="font-size:2.2rem;">🛡️</span>
        <span style="font-size:1.8rem; font-weight:700;"> SpamGuard AI</span>
        <p style="color:#6b7280; margin-top:0.3rem;">
            Detect spam. Protect your inbox. Powered by supervised machine learning.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

if metrics:
    c1, c2, c3 = st.columns(3)
    c1.metric("Model", metrics["best_model"])
    c1_acc = metrics["results"][metrics["best_model"]]["enron_test"]["accuracy"]
    c2.metric("Test accuracy", f"{c1_acc:.1%}")
    c3.metric("Emails learned from", f"{metrics['training_emails']:,}")

st.divider()

if model is None:
    st.error(
        "No trained model found. Run `python train_model.py` inside the "
        "`backend` folder first, then restart this app."
    )
    st.stop()


# ----------------------------------------------------------------------
# Detector
# ----------------------------------------------------------------------
st.subheader("✉️ Check an email")
st.caption("Paste an email's subject and body below, then click Check Email.")

email_text = st.text_area(
    "Email message",
    height=220,
    placeholder="Paste the email text here...",
    label_visibility="collapsed",
)

char_count = len(email_text)
st.caption(f"{char_count} characters")

col_check, col_clear = st.columns([1, 1])
check_clicked = col_check.button("🔍 Check Email", type="primary", use_container_width=True)
clear_clicked = col_clear.button("Clear", use_container_width=True)

if clear_clicked:
    st.session_state.pop("email_input", None)
    st.rerun()

if check_clicked:
    text = email_text.strip()

    if not text:
        st.warning("Please enter an email message.")
    elif len(text) < MIN_CHARS:
        st.warning(f"Please enter a longer email message (at least {MIN_CHARS} characters).")
    elif len(text) > MAX_CHARS:
        st.warning(f"Email text must be at most {MAX_CHARS:,} characters.")
    else:
        with st.spinner("Analyzing email..."):
            spam_probability = float(model.predict_proba([text])[0][1])
            is_spam = spam_probability >= 0.5
            confidence = spam_probability if is_spam else 1.0 - spam_probability

        st.session_state.history.append(
            {"label": "Spam" if is_spam else "Not Spam", "confidence": confidence}
        )

        if is_spam:
            st.error(f"🚫 **Spam Detected**  —  confidence {confidence:.0%}")
            st.write("The machine learning model classified this email as spam.")
        else:
            st.success(f"✅ **Not Spam**  —  confidence {confidence:.0%}")
            st.write("The machine learning model classified this email as not spam.")

        st.progress(spam_probability, text=f"Spam probability: {spam_probability:.0%}")

# ----------------------------------------------------------------------
# Session history
# ----------------------------------------------------------------------
if st.session_state.history:
    with st.expander(f"Checked this session ({len(st.session_state.history)})"):
        for i, item in enumerate(reversed(st.session_state.history), 1):
            icon = "🚫" if item["label"] == "Spam" else "✅"
            st.write(f"{icon} {item['label']} — {item['confidence']:.0%} confidence")

st.divider()

# ----------------------------------------------------------------------
# How it works / About (mirrors the old landing page sections)
# ----------------------------------------------------------------------
with st.expander("⚙️ How it works"):
    st.markdown(
        """
1. **Enter email** — paste or type an email message.
2. **Text processing** — the email text is converted into numerical features (TF-IDF).
3. **ML prediction** — the trained model classifies the email.
4. **View result** — the prediction is shown as Spam or Not Spam, with a confidence score.
        """
    )

with st.expander("ℹ️ About this project"):
    st.markdown(
        """
Email Spam Detection is a supervised machine learning project that identifies whether
an email message is spam or not spam. The model learned from labelled email examples
(the Enron-Spam dataset plus a small team-written dataset) and is applied here to new,
unseen messages.

**Limitations:** the training data is mostly from the early 2000s, so very recent phishing
styles can occasionally be missed. The model looks only at message text — not links,
attachments, or sender reputation.
        """
    )
