import streamlit as st
from groq import Groq

st.image("https://cdn.britannica.com/70/234870-050-D4D024BB/Orange-colored-cat-yawns-displaying-teeth.jpg", caption="Sunrise by the mountains")

province = st.selectbox(
    "How would you like to be contacted?",
    ("ขอนแก่น", "อุดรธานี"),
)


groq_client = Groq(
    api_key="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",
)

models = {
    "gemma2-9b-it": "gemma2-9b-it",
    "mixtral-8x7b-32768": "mixtral-8x7b-32768",
    "llama-3.2-1b-preview": "llama-3.2-1b-preview",
    "llama-3.2-3b-preview": "llama-3.2-3b-preview",
    "llama-3.1-8b-instant": "llama-3.1-8b-instant",
    "llama3-groq-8b-8192-tool-use-preview": "llama3-groq-8b-8192-tool-use-preview",
    "llama3-8b-8192": "llama3-8b-8192",
    "llama-3.2-11b-vision-preview": "llama-3.2-11b-vision-preview",
    "llama3-70b-8192": "llama3-70b-8192",
    "llama-3.3-70b-specdec": "llama-3.3-70b-specdec",
    "llama-3.3-70b-versatile": "llama-3.3-70b-versatile",
    "llama-3.1-70b-versatile": "llama-3.1-70b-versatile",
    "llama-3.2-90b-vision-preview": "llama-3.2-90b-vision-preview"
}

chat_completion = groq_client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "แนะนำสถานที่ท่องเที่ยวภาคอีสานในประเทศไทย เป็นภาษาไทย โดยจัดแผนการท่องเที่ยวหลาย ๆ ตัวเลือก และข้อความมีความดึงดูดให้น่าอ่านน่าสนใจ", # จะให้ agent ตอบแบบไหนอยู่ที่การตั้ง instruction ตรงนี้
        }
    ],
    model=models['gemma2-9b-it'],
)

st.write("You selected:", chat_completion.choices[0].message.content)