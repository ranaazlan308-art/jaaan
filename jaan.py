import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="3 Years & Forever ❤️",
    page_icon="💖",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #FFF0F5;
    }
    h1 {
        color: #D81B60;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    p {
        color: #4A4A4A;
        font-size: 18px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Subtitle
st.title("❤️ To My Future Wife ❤️")
st.write("Hamare 3 saal ke is khoobsurat safar ke naam ek chota sa surprise...")

st.markdown("---")

# Photo Section
# APNI PHOTO KA NAME YAHAN UPDATE KAREN (e.g., "our_pic.jpg")
try:
    image = Image.open("our_pic.jpg")
    st.image(image, caption="3 Saal Ka Khoobsurat Safar & Hamesha Ka Saath 💕", use_column_width=True)
except FileNotFoundError:
    st.info("📌 **Photo Add Karne Ka Tareeqa:** Jis folder me ye script hai, wahan apni picture rakhein aur code me 'our_pic.jpg' naam set kar dein.")

st.markdown("---")

# 3 Years Journey Highlights
st.subheader("🌹 Hamare 3 Saal...")

col1, col2 = st.columns(2)

with col1:
    st.info("⏳ **3 Saal Ki Yaadein**\n1,095 din aur be-shumar haseen pal jo humne saath guzare.")
    st.success("🌸 **Aap Ka Saath**\nIn 3 salon me aapne har mod par mera saath diya.")

with col2:
    st.warning("🔮 **Mera Future**\nInshaAllah, bohot jald aap meri biwi banein gi.")
    st.error("💖 **Mera Hamesha Ka Pyar**\nPehle din se lekar aaj tak, mera pyar aapke liye sirf badha hai.")

st.markdown("---")

# Heartfelt Romantic Message Box
st.markdown("""
<div style="background-color: #ffe6e8; padding: 20px; border-radius: 15px; border: 2px solid #ff4d6d; text-align: center;">
    <h3 style="color: #c9184a;">💌 Ek Dil Se Paigham</h3>
    <p style="font-size: 18px; color: #590d22;">
        "3 saal pehle jab aap meri zindagi me aayi thi, tab se lekar aaj tak har din khas ban gaya hai. 
        Main sab se zyada khush-kismat hoon ke aap meri life partner banne ja rahi hain. 
        Meri life ki sab se haseen khwahish aap hain!"
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# Interactive Magic Surprise Button
st.subheader("👉 Yahan Click Karein:")

if st.button("💖 Click For Special Surprise! 💖"):
    # Celebration Animation
    st.balloons()
    
    st.markdown("""
        <h2 style='text-align: center; color: #ff0054;'>
            I LOVE YOU SO MUCH! 💍💕
        </h2>
        <p style='text-align: center; font-weight: bold; font-size: 20px;'>
            Aap se shaadi karne ka me besabri se intezar kar raha hoon! ❤️
        </p>
    """, unsafe_allow_html=True)
    
    st.snow()