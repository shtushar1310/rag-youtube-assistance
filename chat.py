from ingest import ingest
from rag_chain import build_chain

url =input("")
ingest(url)

chain = build_chain()

while True:
    question = input("\nYou: ")
    if question.lower() in ("exit", "quit"):
        break
    result = chain.invoke(question)
    print(f"\nAssistant: {result}")


## Key decisions to make