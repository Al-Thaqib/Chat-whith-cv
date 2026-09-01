import os
from dotenv import load_dotenv
from openai import OpenAI
import docx

load_dotenv(override=True)
openai_api_key = os.getenv("OPEN_AI_API_KEY")

cv_text = []
doc = docx.Document('my_cv.docx')
for page in doc.paragraphs:
    cv_text.append(page.text)
cv_readable = '\n'.join(cv_text)

sytem_prompt = f"""
    you are my assistant. you are responsible to reply to questions about my career.
    you have my cv here:\n{cv_readable}. use it to reply
    """
model_name = 'openai/gpt-4o-mini'
LLM = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openai_api_key
)

while True:
    user_prompt = input("whatis your question?\n")
    if user_prompt == 'exit':
        break
    messages = [
        {"role": "system", "content": sytem_prompt},
        {"role": "user", "content": user_prompt}
    ]
    response = LLM.chat.completions.create(
        model=model_name,
        messages=messages
    )
    reply_from_ai = response.choices[0].message.content
    print(reply_from_ai)

