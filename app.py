from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

# load .env file
load_dotenv()

llm = OpenAI(
    model="text-davinci-003",
    temperature=0.9
)

text="Suggest a personalized workout routine for someone looking to improve cardiovascular endurance and prefers in-door activities. "

print(llm(text))