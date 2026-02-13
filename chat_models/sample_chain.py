from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
prompt = PromptTemplate(
    template="Create 3 medium-level math word problems based on the topic: {topic}",
    input_variables=["topic"]
)

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # ✅ change here
    temperature=0.9,
    max_retries=2,
)
# model = ChatOpenAI(model="gpt-5-nano", temperature=0.8)
parser = StrOutputParser()
# Pipeline → prompt → model → parser. # | => pipe symbol /runnable operator
chain = prompt | model | parser

result = chain.invoke({"topic": "Time and Work"})
print(result)
# Show graph
chain.get_graph().print_ascii()