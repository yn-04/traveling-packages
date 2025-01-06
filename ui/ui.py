import streamlit as st
from PIL import Image
from groq import Groq
import openai
import os
from dotenv import load_dotenv
from openai import OpenAI
import base64
from huggingface_hub import InferenceClient


# === Set Layout of Streamlit ===
st.set_page_config(page_title="แนะนำแผนการท่องเที่ยว", page_icon="🌍", layout="wide")

# === Load API Keys ===
load_dotenv()
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
openai_api_key = os.getenv("OPENAI_API_KEY")

# พาธของไฟล์ภาพพื้นหลัง
background_image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ระบบแนะนำแผนการท่องเที่ยว.png")

# ฟังก์ชันสำหรับแปลงไฟล์ภาพเป็น Base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ตรวจสอบว่าไฟล์ภาพพื้นหลังมีอยู่
if os.path.exists(background_image_path):
    # แปลงภาพเป็น Base64
    base64_image = get_base64_of_bin_file(background_image_path)
    
    # ใส่ CSS เพื่อเพิ่มภาพพื้นหลัง
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_image}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            font-family: 'Arial', sans-serif;
            color: #333;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.error("ไม่พบไฟล์ภาพพื้นหลัง กรุณาตรวจสอบชื่อไฟล์และตำแหน่งไฟล์!")
st.markdown(
    f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
    <style>
    .stApp {{
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        font-family: 'Arial', sans-serif;
        color: #333;
    }}
    .spacing {{
        margin-top: 70px;
    }}
    .distance {{
        margin-top: 15px;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }}
    .header {{
        text-align: center;
        margin-bottom: 30px;
        color: white;
    }}
    .result-box {{
        border: 2px solid #ddd;
        padding: 20px;
        border-radius: 12px;
        background-color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease-in-out;
    }}
    .result-box:hover {{
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# === Header ===
st.markdown("<h1 class='header' style='color: white;'>ระบบแนะนำแผนการท่องเที่ยว</h1>", unsafe_allow_html=True)

# === Input Form ===
with st.container():  # ใช้ container เป็นกล่องรอบคอลัมน์
    st.markdown('<div class="form-container">',unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1.5])

    with col1:
        st.markdown("<div class='distance' style='color: white;'><i class='bi bi-geo-alt'></i> Where to?</div>", unsafe_allow_html=True)
        province = st.selectbox("", ["ขอนแก่น", "นครพนม", "นครศรีธรรมราช", "บุรีรัมย์", "เลย"])

    with col2:
        st.markdown("<div class='distance' style='color: white;'><i class='bi bi-calendar'></i> Days </div>", unsafe_allow_html=True)
        days = st.number_input("", min_value=1, step=1, value=3, format="%d")

    with col3:
        st.markdown("<div class='distance' style='color: white;'><i class='bi bi-compass'></i> Types</div></div>",unsafe_allow_html=True,)
        activity_type = st.multiselect("", ["ธรรมชาติ", "เมือง", "วัฒนธรรม", "เอกซ์ตรีม", "ชิล ๆ คาเฟ่"])

    with col4:
        st.markdown("<div class='distance' style='color: white;'><i class='bi bi-cash'></i> Price</div>", unsafe_allow_html=True)
        budget = st.selectbox("", ["Low to High", "Hight to Low"])
        

    with col5:
        st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)
        search = st.button("Search", key="search")
    st.markdown("</div>", unsafe_allow_html=True) 

# Helper function สำหรับแปลงรูปภาพเป็น Base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string
# === Helper Function: Encode Image to Base64 ===
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

# === Generate Image ===
def generate_image(prompt):
    image_dir_name = "images"
    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), image_dir_name)
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)
    
    client = InferenceClient(
        "strangerzonehf/Flux-Midjourney-Mix2-LoRA", token="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"
    )
    image = client.text_to_image(prompt)
    image_path = os.path.join(image_dir, "generated_image.png")
    image.save(image_path)
    return image_path


# === แสดงผลพร้อมรูปภาพในกรอบ ===
if search:
    if not province or not days or not activity_type or not budget:
        st.error("กรุณาเลือกข้อมูลให้ครบทุกช่องก่อนเริ่มค้นหา!")
    else:
        with st.spinner("กำลังประมวลผล..."):
            try:
                # === สร้างข้อความคำถามสำหรับ Groq ===
                query = f"""
                ช่วยแนะนำแผนการท่องเที่ยวในจังหวัด {province} 
                สำหรับจำนวน {days} วัน งบประมาณ {budget} บาท 
                และประเภทการเที่ยว {', '.join(activity_type)}
                """
                chat_completion = groq_client.chat.completions.create(
                    messages=[{"role": "user", "content": query}],
                    model="llama-3.1-70b-versatile",
                )
                travel_plan = chat_completion.choices[0].message.content

                # === Generate Image ===
                translated_prompt = f"Travel plan for {province} with {days} days: {travel_plan}"
                image_path = generate_image(translated_prompt)
                base64_image = encode_image_to_base64(image_path)

                # แสดงผลพร้อมรูปภาพในกรอบ
                st.markdown("<h6 style = 'color: white;'>แผนการท่องเที่ยวที่แนะนำ</h6>", unsafe_allow_html=True)
                st.markdown(
                    f"""
                    <div class='result-box'>
                        <img src='data:image/png;base64,{base64_image}' alt='รูปภาพสถานที่ท่องเที่ยว' 
                             style='width:100%; border-radius:8px; margin-bottom:15px;'>
                        <div style='color: black;'>{travel_plan}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
