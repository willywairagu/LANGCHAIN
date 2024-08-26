import os
from dotenv import load_dotenv

from langchain.llms import OpenAI

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def main():
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)

    result = llm.predict("What is self analytics?")

    print(result)

if __name__ == "__main__":
    main()
    