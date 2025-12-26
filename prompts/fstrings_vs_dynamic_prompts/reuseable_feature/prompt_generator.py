from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
    Explain in {lines} lines about {topic}
    """,
    input_variables=['lines', 'topic'],
    validate_template=True)

template.save("template.json")