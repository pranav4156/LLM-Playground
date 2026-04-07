from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")  # free & fast

result = llm.invoke("what is position in sex?")
print(result.content)