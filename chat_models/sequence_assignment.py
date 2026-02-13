from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
prompt1 = PromptTemplate(
    template="summarise the given tasxt intop 3-4 line{prompt}",
    input_variables=['prompt']  
)
prompt2 = PromptTemplate(
    template="extract 5 point from this summary:\n{text}",
    input_variables=['text']
)
model =ChatOpenAI(model="gpt-5-nano", temperature=0.8)
model1=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.5,
    max_retries=2,
)
parser = StrOutputParser()
chain = prompt1 | model | parser | prompt2 | model1 | parser
result = chain.invoke({"prompt":"Generative artificial intelligence (generative AI) is a type of AI that can create new content and ideas, including conversations, stories, images, videos, and music. It can learn human language, programming languages, art, chemistry, biology, or any complex subject matter"})
print(result)
chain.get_graph().print_ascii()