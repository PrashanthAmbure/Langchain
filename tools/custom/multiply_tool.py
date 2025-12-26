from langchain_core.tools import tool

@tool
def multiply(a: int, b:int) -> int:
    """Multiply two integer numbers and return the product of the two numbers which will also be int"""
    return a*b

result = multiply.invoke({'a': 3, 'b': 5})

print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)

print(multiply.args_schema.model_json_schema())