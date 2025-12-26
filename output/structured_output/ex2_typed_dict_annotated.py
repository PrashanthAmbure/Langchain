from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated, Optional, Literal

# Annotated helps us with following.
# 1. Unlike ex1 where we just defined summary or sentiment, llm might not understand what exactly to do, it might get halucinated, hence we need a way to let llm know that what summary means and what sentiment means. This canbe achived by Annoatated.
# 2. We can define them to optional
# 3.We can define the output that it generateds what it can contain like for sentiment instead of returning positive negative, return Pos or NEG

# Drawaback:
# Although we mentioned summaryt to be string there is no guarantee llm would return str only it may do mistake return list, possible.
# Assume we have rating and we say llm to show rating only when it is greater than 3 but llm might make mistake and display less than 3 ratings as well.
# So data validations cannot be done here we have to go for Pydantic. TypedDict is only for representation.


#Schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the Review"]
    sentiment: Annotated[Literal["pos","neg"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "This is optional if cons do not exists, can skip else write down all the cons inside a list"]

model = ChatOllama(model='llama3')

structured_model=model.with_structured_output(Review)

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