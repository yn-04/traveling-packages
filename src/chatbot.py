from groq import Groq

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
            "content": "แนะนำสถานที่ท่องเที่ยวในประเทศไทย เป็นภาษาไทย",
        }
    ],
    model=llama_8b,
)

print(chat_completion.choices[0].message.content)