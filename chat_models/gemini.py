from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   # ✅ change here
    temperature=0.9,
    max_retries=2,
)

result = model.invoke("write 5 lines poem on global engineering college jabalpur")

print("\n")
print(result.content)   # ✅ .content print karo
print("\n")
