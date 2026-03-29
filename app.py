# file: app.py

import streamlit as st
import random


def classify(num: int) -> str:
    return "SMALL" if num <= 4 else "BIG"


def generate_result():
    num = random.randint(0, 9)
    size = classify(num)
    color = "Green" if size == "BIG" else "Red"
    return num, size, color


# UI config
st.set_page_config(page_title="Instant Result Tool", layout="centered")

st.title("⚡ Instant Result Tool")

# session state to persist result
if "result" not in st.session_state:
    st.session_state.result = generate_result()

# display result
num, size, color = st.session_state.result

st.markdown("### 🎯 Result")
st.write(f"Number: {num}")

if size == "BIG":
    st.markdown(f"<h2 style='color:#00ffcc'>{size}</h2>", unsafe_allow_html=True)
else:
    st.markdown(f"<h2 style='color:#ff4b4b'>{size}</h2>", unsafe_allow_html=True)

st.write(f"Colour: {color}")

# one tap button
if st.button("🎲 Generate New"):
    st.session_state.result = generate_result()
    st.rerun()
