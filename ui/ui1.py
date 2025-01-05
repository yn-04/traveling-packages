import streamlit as st
from PIL import Image  # used to print and edit images
from groq import Groq
import openai
import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

# === โหลดค่า API Key จาก .env ===
load_dotenv()
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
openai_api_key = os.getenv("OPENAI_API_KEY")

# ตรวจสอบ API Key
if not openai_api_key:
    print("API Key is missing from .env")
else:
    print("API Key loaded successfully")

# === ตั้งค่า Layout ของ Streamlit ===
st.set_page_config(
    page_title="แนะนำแผนการท่องเที่ยว",
    page_icon="🌍",
    layout="wide",
)

# === โหลดรูปพื้นหลังจาก URL โดยตรง ===
background_image_url = "https://cbtthailand.dasta.or.th/upload-file-api/Resources/RelateAttraction/Images/RAT400021/1.jpeg"

st.markdown(
    f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
    <style>
    .stApp {{
        background-image: url('{background_image_url}');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}
    .spacing {{
        margin-top: 55px;
    }}
    .distance {{
        margin-bottom: 0px;
        padding-bottom: 0px;
    }}
    .info-box {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# === ส่วนหัวของเว็บไซต์ ===
st.markdown("<h1 style='text-align: center;'>🌟 ระบบแนะนำแผนการท่องเที่ยว</h1>", unsafe_allow_html=True)

# === ส่วน UI ค้นหาข้อมูล ===

st.markdown('<div class="info-box">', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])

with col1:
    st.markdown("<div class='distance'><i class='bi bi-geo-alt'></i> Where to?</div>", unsafe_allow_html=True)
    province = st.selectbox("", ["ขอนแก่น", "นครพนม", "นครศรีธรรมราช", "บุรีรัมย์", "เลย"])

with col2:
    st.markdown("<div class='distance'><i class='bi bi-calendar'></i> Days</div>", unsafe_allow_html=True)
    days = st.number_input("", min_value=1, step=1, value=3, format="%d")

with col3:
    st.markdown("<div class='distance'><i class='bi bi-compass'></i> Type</div>", unsafe_allow_html=True)
    activity_type = st.selectbox("", ["ธรรมชาติ", "เมือง", "วัฒนธรรม", "เอกซ์ตรีม", "ชิล ๆ คาเฟ่"])

with col4:
    st.markdown("<div class='distance'><i class='bi bi-cash'></i> Price</div>", unsafe_allow_html=True)
    budget = st.selectbox("", ["Low to High", "Hight to Low"])

with col5:
    st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)
    search = st.markdown("<button style='width:100%;padding:5px;border:none;background:gray;color:white;border-radius:5px;'><i class='bi bi-search'></i></button>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# === ปุ่มค้นหาแผนการท่องเที่ยว ===
if search:
    with st.spinner("กำลังประมวลผล..."):
        try:
            # === สร้างข้อความคำถามสำหรับ Groq ===
            query = f"""
            ช่วยแนะนำแผนการท่องเที่ยวในจังหวัด {province} 
            สำหรับจำนวน {days} วัน งบประมาณ {budget} บาท 
            และประเภทการเที่ยว {activity_type}
            """
            chat_completion = groq_client.chat.completions.create(
                messages=[{"role": "user", "content": query}],
                model="llama-3.1-70b-versatile",
            )

            # === แสดงผลแผนการท่องเที่ยว ===
            
            st.subheader("✨ แผนการท่องเที่ยวที่แนะนำ:")
            st.success(chat_completion.choices[0].message.content)
            st.markdown('</div>', unsafe_allow_html=True)

            # === เพิ่มการเจนรูปภาพ ===
            with st.spinner("กำลังสร้างภาพสถานที่..."):
                # สร้าง prompt สำหรับการเจนรูปภาพ
                prompt = f"""
                ภาพสถานที่ท่องเที่ยวในจังหวัด {province} 
                ที่เหมาะสำหรับการท่องเที่ยว {activity_type} 
                เป็นเวลา {days} วัน
                """
                client = OpenAI(api_key=openai_api_key)

                # เรียก OpenAI API เพื่อสร้างรูปภาพ
                generation_response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    n=1,
                    size="1024x1792",
                )

                # ดึง URL ของรูปภาพ
                image_url = generation_response.data[0].url
                st.image(image_url, caption=f"ภาพสถานที่ใน {province} ({activity_type})")

        except Exception as e:
            st.error(f"เกิดข้อผิด: {e}")


# === ส่วนท้ายเว็บไซต์ ===
st.markdown(
    """
    <hr style="border: 1px solid #ccc;">
    <footer style="text-align: center; color: #777; font-size: 0.9rem;">
        © 2025 ระบบแนะนำแผนการท่องเที่ยว | พัฒนาโดย Yuki
    </footer>
    """,
    unsafe_allow_html=True,
)
