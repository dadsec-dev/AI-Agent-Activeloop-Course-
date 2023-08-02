from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# load .env file
load_dotenv()


llm = OpenAI(model="text-davinci-003", temperature=0.9)

prompt = PromptTemplate(
    input_variables=["description"],
    template="What is a good name for a badass {description}?",
)

chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain only specifying the input variable.
print(chain.run("Smart Contract developer and onchain security analyst ?"));