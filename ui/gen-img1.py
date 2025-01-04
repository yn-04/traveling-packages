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
    page_icon="🗺️",
    layout="wide",
)

# === ส่วนหัวของเว็บไซต์ ===
st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
    <style>
    .stApp {
        background-image: url('https://cdn.pixabay.com/photo/2016/11/29/03/20/thailand-1867228_1280.jpg');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    .search-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 10%;
        padding: 20px;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .search-input {
        margin: 0 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align: center;'>🌟 ระบบแนะนำแผนการท่องเที่ยว</h1>", unsafe_allow_html=True)

# === ส่วน UI ค้นหาข้อมูล ===
st.markdown('<div class="search-container">', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])

with col1:
    province = st.selectbox("Where to?", ["ขอนแก่น", "นครพนม", "นครศรีธรรมราช", "บุรีรัมย์", "เลย"])

with col2:
    days = st.number_input("Days", min_value=1, step=1, value=3, format="%d")

with col3:
    activity_type = st.selectbox("Type", ["ธรรมชาติ", "เมือง", "วัฒนธรรม", "เอกซ์ตรีม", "ชิล ๆ คาเฟ่"])

with col4:
    budget = st.number_input("Price", min_value=0, step=100, value=5000, format="%d")

with col5:
    search = st.markdown("<button style='width:100%;padding:5px;border:none;background:gray;;color:white;border-radius:5px;'><i class='bi bi-search'></i></button>", unsafe_allow_html=True)

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
            st.markdown('<div class="info-box">', unsafe_allow_html=True)
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

                # สร้างไดเรกทอรีสำหรับเก็บรูปภาพ
                image_dir_name = "images"
                image_dir = os.path.join(os.getcwd(), image_dir_name)
                if not os.path.isdir(image_dir):
                    os.mkdir(image_dir)

                # บันทึกรูปภาพ
                generated_image_name = f"{province}_{activity_type}.png"
                generated_image_filepath = os.path.join(image_dir, generated_image_name)
                generated_image = requests.get(image_url).content

                with open(generated_image_filepath, "wb") as image_file:
                    image_file.write(generated_image)

                # แสดงภาพที่สร้าง
                st.image(generated_image_filepath, caption=f"ภาพสถานที่ใน {province} ({activity_type})")

        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {e}")

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