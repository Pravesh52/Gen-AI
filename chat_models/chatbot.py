from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Model configuration
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # ✅ change here
    temperature=0.9,
    max_retries=2,
)

# Initial system message for bot personality
messages = [SystemMessage(content="You are a funny bot")]

print("LET'S RESOLVE YOUR QUERIES (type 'quit' to exit)\n")

while True:
    user_input = input("User: ")
    
    if user_input.lower() == "quit":
        break
    
    # Append human message
    messages.append(HumanMessage(content=user_input))
    
    # Get AI response
    result = model.invoke(messages)
    
    # Append AI message
    messages.append(AIMessage(content=result.content))
    
    print("Bot:", result.content, "\n")
