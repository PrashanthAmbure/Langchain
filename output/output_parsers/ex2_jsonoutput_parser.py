from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

model=ChatOllama(model="gemma3")
# The drawback of this parser is we can't define the schema of the output like the way we want, it will be decided by llm. If we want o define schema of the output then StructureOutputParser.
parser = JsonOutputParser()

template1 = PromptTemplate(
    template="""
    Give me the name, age and city of a fictional person \n {format_instruction}
    """,
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()},
    validate_template=True
)

chain = template1 | model | parser

response = chain.invoke({})

print(f"Response: {response}")

