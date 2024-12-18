import streamlit as st
from groq import Groq

st.image("https://cdn.britannica.com/70/234870-050-D4D024BB/Orange-colored-cat-yawns-displaying-teeth.jpg", caption="Sunrise by the mountains")

province = st.selectbox(
    "How would you like to be contacted?",
    ("ขอนแก่น", "อุดรธานี", "นครพนม", "พิษณุโลก"),
)

text_input = st.text_input("Enter some text 👇")
print(text_input)

groq_client = Groq(
    api_key="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",
)

llama_70B = "llama-3.1-70b-versatile"
llama_405B = "llama-3.1-405b-reasoning"
llama_8b = "llama3-8b-8192"


chat_completion = groq_client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"{text_input}",
        }
    ],
    model=llama_70B,
)

st.write("You selected:", chat_completion.choices[0].message.content)