from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model='gemma3:12b')


schema = [
    ResponseSchema(name='fact_1', description="Fact 1 about the topic"),
    ResponseSchema(name='fact_2', description="Fact 2 about the topic"),
    ResponseSchema(name='fact_3', description="Fact 3 about the topic")
]

# Drawback is we can't validate data eg, if age is int but llm can retruies it as 35 years which is strung and not int, hence we go for pydantic o/p parser
parser = StructuredOutputParser.from_response_schemas(schema)

template1 = PromptTemplate(
    template="""
    Give 3 facts about {topic} \n {format_instructions}
    """,
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()},
    validate_template=True
)

chain = template1 | model | parser

response = chain.invoke({'topic': 'Black Hole'})

print(f"Response: {response}")
