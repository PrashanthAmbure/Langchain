from langchain_ollama import ChatOllama
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int


# person: Person = {'name': 'Prashanth', 'age': '35'}
person: Person = {'name': 32, 'age': '35'} # Though it is string it will still accept, TypedDict is only for representation i.e for the for one who is using he can look what type of fields to pass but it won't validate. To do validation use Pydantic

print(f"Person: {person}")

#Schema
class Review(TypedDict):
    summary: str
    sentiment: str

model = ChatOllama(model='llama3')

structured_model=model.with_structured_output(Review)

response = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many installed apps, which I can't remove. Also the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(f"Type of Response: {type(response)}")
print(f"Response: {response}")
print(f"Sentiment: {response['sentiment']}")