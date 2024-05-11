from getpass import getpass
from langchain_community.llms import Cohere
import os

#Authorise access with LLM API Key as password
COHERE_API_KEY=getpass()

#Establish connection to llm
llm2 = Cohere(cohere_api_key=COHERE_API_KEY)

print("Lets start!")

moreQue = True

#Iterate to keep asking question
while moreQue:
    print("How can I help you?", end="\n")
    prompt = input()
    print(llm2(prompt))
    choice = input("Have more questions?(y/n)")
    if choice == "n":
        moreQue = False