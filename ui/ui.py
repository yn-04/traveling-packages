import streamlit as st
from groq import Groq

# ตั้งค่า API Key
groq_client = Groq(
    api_key="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",
)

# UI ของ Streamlit
st.title("ระบบแนะนำแผนการท่องเที่ยว")

st.image(
    "https://cdn.britannica.com/70/234870-050-D4D024BB/Orange-colored-cat-yawns-displaying-teeth.jpg", 
    caption="ภาพประกอบ - การท่องเที่ยว"
)

# เลือกข้อมูลที่ต้องการ
province = st.selectbox(
    "เลือกจังหวัดที่ต้องการท่องเที่ยว",
    ("ขอนแก่น", "อุดรธานี", "นครพนม", "พิษณุโลก", "บุรีรัมย์"),
)

days = st.slider(
    "จำนวนวันที่คุณต้องการไปเที่ยว", 
    min_value=1, 
    max_value=7, 
    value=3
)

budget = st.number_input(
    "กรอกงบประมาณ (บาท)", 
    min_value=1000, 
    step=1000, 
    value=5000
)

activity_type = st.selectbox(
    "เลือกประเภทสถานที่ที่ต้องการเที่ยว",
    ("ธรรมชาติ", "เมือง", "วัฒนธรรม", "เอกซ์ตรีม", "ชิล ๆ คาเฟ่")
)

# ดึงข้อมูลจาก Groq
if st.button("ค้นหาแผนการท่องเที่ยว"):
    try:
        query = f"""
        ช่วยแนะนำแผนการท่องเที่ยวในจังหวัด {province} 
        สำหรับจำนวน {days} วัน งบประมาณ {budget} บาท 
        และประเภทการเที่ยว {activity_type}
        โดยให้แผนดูน่าสนใจและเหมาะกับผู้ใช้
        """
        chat_completion = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": query}],
            model="llama-3.1-70b-versatile",
        )

        # แสดงผลลัพธ์
        st.subheader("แผนการท่องเที่ยวที่แนะนำ:")
        st.success(chat_completion.choices[0].message.content)

    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")