import streamlit as st
import os
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="3 Years & Forever ❤️",
    page_icon="💖",
    layout="centered"
)

# 2. Custom CSS Styling
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

# 3. Main Title
st.title("❤️ To My Future Wife ❤️")
st.write("Hamare 3 saal ke is khoobsurat safar ke naam ek chota sa surprise...")

st.markdown("---")

# 4. Safe Image Loader (Prevents UnidentifiedImageError & Crashes)
script_dir = os.path.dirname(os.path.abspath(__file__))

# File ka naam exact GitHub wali file se match karein
image_path = os.path.join(script_dir, "our_pic.jpeg") 

if os.path.exists(image_path):
    try:
        # PIL image load and safe RGB conversion
        with Image.open(image_path) as raw_img:
            img = raw_img.convert("RGB")
            st.image(img, caption="3 Saal Ka Khoobsurat Safar & Hamesha Ka Saath 💕", use_container_width=True)
    except Exception:
        # Fallback if PIL fails: Display direct path
        try:
            st.image(image_path, caption="3 Saal Ka Khoobsurat Safar & Hamesha Ka Saath 💕", use_container_width=True)
        except Exception:
            st.warning("⚠️ Photo display karne me masla aa raha hai. File extension check karein.")
else:
    st.error("⚠️ Photo file nahi mili! File ka naam GitHub par 'our_pic.jpeg' hi rakhein.")

st.markdown("---")

# 5. Relationship Journey Highlights
st.subheader("🌹 Hamare 3 Saal...")

col1, col2 = st.columns(2)

with col1:
    st.info("⏳ **3 Saal Ki Yaadein**\n1,095 din aur be-shumar haseen pal jo humne saath guzare.")
    st.success("🌸 **Aap Ka Saath**\nIn 3 salon me aapne har mod par mera saath diya.")

with col2:
    st.warning("🔮 **Mera Future**\nInshaAllah, bohot jald aap meri biwi banein gi.")
    st.error("💖 **Mera Hamesha Ka Pyar**\nPehle din se lekar aaj tak, mera pyar aapke liye sirf badha hai.")

st.markdown("---")

# 6. Romantic Love Note
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

# 7. Surprise Button
st.subheader("👉 Neeche Diye Gaye Button Par Click Karein:")

if st.button("💖 Click For Special Surprise! 💖"):
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
