from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda

model = ChatOllama(model='llama3.1')

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of the feedback")

str_parser = StrOutputParser()
feedback_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback', 'format_instruction'],
    partial_variables={'format_instruction': feedback_parser.get_format_instructions()},
    validate_template=True
)

classifier_chain = prompt1 | model | feedback_parser

response = classifier_chain.invoke({'feedback': 'This is a terrible smartphone'})

print(response.sentiment)

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback'],
    validate_template=True
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback'],
    validate_template=True
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | str_parser),
    (lambda x:x.sentiment== 'negative', prompt3 | model | str_parser),
    RunnableLambda(lambda x: 'Could not find sentiment')
)

chain = classifier_chain | branch_chain

response = chain.invoke({'feedback': 'This is a terrible smartphone'})

print(response)

print(chain.get_graph().draw_ascii())


