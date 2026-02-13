from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   # ✅ change here
    temperature=0.9,
    max_retries=2,
)
message=[SystemMessage(content="You are a funny bot "),HumanMessage(content="tell me a joke about Gen Ai")]
result =model.invoke(message)
message.append(AIMessage(content=result.content))
print(message)