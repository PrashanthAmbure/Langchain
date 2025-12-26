import json

from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field



# Schema
schema = ''
with open('json_schema.json', 'r', encoding="utf-8") as f:
    schema = json.load(f)


model = ChatOllama(model='llama3')

structured_model = model.with_structured_output(schema)

response = structured_model.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, its an absolute power house! The snapdragon 8 Gen 3 processor makes everything lightning fast-weather I'm gaming, multitasking, or editing photos. The 500mAH battery easily
lasts a full day even with heavy use, and the 45w fast charging is a life saver.

The S-Pen integration is a great touch for note-taking a quick sketches, though I don't use it often. What really blew me away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 
100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard
pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful.

Cons:
Bulky and heavy-not great for one-handed use
Bloatware still exists in one UI
Expensive compared to competitors  

""")

# print(f"Type of Response: {type(response)}")
print(f"Response: {response}")
# print(f"Sentiment: {response['sentiment']}")