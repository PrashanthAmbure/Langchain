from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

model = ChatOllama(model='gemma3:12b')

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description="Name of the city person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="""
    Generate name, age and city of fictional {place} person \n {format_instructions}
    """,
    validate_template=True,
    input_variables=['place'],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

print(f"Prompt={template.invoke({'place': 'India'})}")

chain = template | model | parser

response = chain.invoke({'place': 'India'})

print(f"Response: {response}")
