import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="3 Years & Forever ❤️",
    page_icon="💖",
    layout="centered"
)

# 2. Custom CSS Styling (Romantic, Premium & Highly Readable Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Nunito:wght@400;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap');

    /* Main App Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #fff0f3 0%, #ffccd5 50%, #ffb3c1 100%);
        font-family: 'Nunito', sans-serif;
    }

    /* Main Title Styling */
    .main-title {
        font-family: 'Great Vibes', cursive;
        color: #800f2f;
        text-align: center;
        font-size: 54px !important;
        font-weight: bold;
        margin-bottom: 0px;
        text-shadow: 2px 2px 4px rgba(255, 182, 193, 0.6);
    }

    .sub-title {
        font-family: 'Playfair Display', serif;
        color: #590d22;
        text-align: center;
        font-size: 19px;
        font-style: italic;
        margin-top: -5px;
        margin-bottom: 25px;
        font-weight: 600;
    }

    /* Section Headers */
    .section-header {
        font-family: 'Playfair Display', serif;
        color: #800f2f;
        text-align: center;
        font-size: 26px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* Romantic Feature Cards Grid */
    .card-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
        margin-bottom: 25px;
    }

    @media (max-width: 600px) {
        .card-grid {
            grid-template-columns: 1fr;
        }
    }

    .journey-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 8px 20px rgba(128, 15, 47, 0.1);
        border-left: 5px solid #c9184a;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .journey-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 25px rgba(128, 15, 47, 0.18);
    }

    .journey-card h4 {
        color: #a4133c;
        font-family: 'Playfair Display', serif;
        font-size: 19px;
        margin: 0 0 8px 0;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .journey-card p {
        color: #2b0914;
        font-size: 15px;
        line-height: 1.5;
        margin: 0;
        font-weight: 700;
    }

    /* Romantic Love Letter Box */
    .love-letter {
        background: linear-gradient(135deg, #ffffff 0%, #fff0f3 100%);
        padding: 28px 24px;
        border-radius: 20px;
        border: 2px solid #ff4d6d;
        box-shadow: 0 10px 25px rgba(201, 24, 74, 0.12);
        text-align: center;
        margin: 25px 0;
    }

    .love-letter h3 {
        font-family: 'Great Vibes', cursive;
        color: #c9184a;
        font-size: 40px;
        margin: 0 0 12px 0;
    }

    .love-letter p {
        font-family: 'Playfair Display', serif;
        font-size: 18px;
        color: #590d22;
        line-height: 1.7;
        margin: 0;
        font-weight: 600;
    }

    /* Custom Styled Streamlit Button */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #ff0054, #ff5400);
        color: #ffffff !important;
        font-family: 'Nunito', sans-serif;
        font-size: 20px !important;
        font-weight: 800 !important;
        padding: 14px 28px !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 8px 20px rgba(255, 0, 84, 0.35) !important;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s ease !important;
    }

    div.stButton > button:first-child:hover {
        background: linear-gradient(45deg, #ff5400, #ff0054);
        box-shadow: 0 12px 28px rgba(255, 0, 84, 0.5) !important;
        transform: scale(1.02);
    }

    /* Surprise Banner */
    .surprise-box {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 25px;
        border: 3px dashed #ff0054;
        text-align: center;
        margin-top: 25px;
    }

    .surprise-title {
        font-family: 'Great Vibes', cursive;
        color: #ff0054;
        font-size: 48px;
        margin: 0;
    }

    .surprise-text {
        font-family: 'Playfair Display', serif;
        color: #590d22;
        font-size: 20px;
        font-weight: 700;
        margin-top: 10px;
    }

    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(to right, transparent, #ff4d6d, transparent);
        margin: 30px 0;
    }

    /* Image Styling */
    .stImage > img {
        border-radius: 20px;
        box-shadow: 0 12px 30px rgba(128, 15, 47, 0.2);
        border: 4px solid #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Main Title Section
st.markdown('<div class="main-title">❤️ To My Future Wife ❤️</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Hamare 3 saal ke is khoobsurat safar ke naam ek chota sa surprise...</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 4. Direct Online Photo Loader
IMAGE_URL = "https://i.ibb.co/prN12tqV/our-pi.jpg"

try:
    st.image(
        IMAGE_URL, 
        caption="3 Saal Ka Khoobsurat Safar & Hamesha Ka Saath 💕", 
        use_container_width=True
    )
except Exception:
    st.markdown('<p style="text-align:center; font-size:20px; color:#800f2f; font-weight:bold;">❤️ 3 Saal Ka Khoobsurat Safar ❤️</p>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 5. Relationship Journey Highlights
st.markdown('<div class="section-header">🌹 Hamare 3 Saal...</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card-grid">
    <div class="journey-card" style="border-left-color: #c9184a;">
        <h4>⏳ 3 Saal Ki Yaadein</h4>
        <p>1,095 din aur be-shumar haseen pal jo humne saath guzare.</p>
    </div>
    <div class="journey-card" style="border-left-color: #ff4d6d;">
        <h4>🌸 Aap Ka Saath</h4>
        <p>In 3 salon me aapne har mod par mera saath diya.</p>
    </div>
    <div class="journey-card" style="border-left-color: #ff758f;">
        <h4>🔮 Mera Future</h4>
        <p>InshaAllah, bohot jald aap meri biwi banein gi.</p>
    </div>
    <div class="journey-card" style="border-left-color: #ffb3c1;">
        <h4>💖 Mera Hamesha Ka Pyar</h4>
        <p>Pehle din se lekar aaj tak, mera pyar aapke liye sirf badha hai.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 6. Romantic Love Note
st.markdown("""
<div class="love-letter">
    <h3>💌 Ek Dil Se Paigham</h3>
    <p>
        "3 saal pehle jab aap meri zindagi me aayi thi, tab se lekar aaj tak har din khas ban gaya hai. 
        Main sab se zyada khush-kismat hoon ke aap meri life partner banne ja rahi hain. 
        Meri life ki sab se haseen khwahish aap hain!"
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# 7. Surprise Button
st.markdown('<div class="section-header">👉 Neeche Diye Gaye Button Par Click Karein:</div>', unsafe_allow_html=True)

if st.button("💖 Click For Special Surprise! 💖"):
    st.balloons()
    st.snow()
    
    st.markdown("""
    <div class="surprise-box">
        <div class="surprise-title">I LOVE YOU SO MUCH! 💍💕</div>
        <div class="surprise-text">
            Aap se shaadi karne ka me besabri se intezar kar raha hoon! ❤️
        </div>
    </div>
    """, unsafe_allow_html=True)
