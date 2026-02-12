from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   # ✅ change here
    temperature=0.9,
    max_retries=2,
)
history=[]
print("LET'S RESOLVE YOUR QUERIES \n")
while True:
    text=input("user: ")
    history.append(text)
    if text=="quit":
        break
    result=model.invoke(history)
    history.append(result.content)
    print("Bot : ", result.content,"\n\n")


