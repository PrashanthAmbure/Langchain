from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

@tool
def multiply(a: int, b:int) -> int:
    """Multiply two integer numbers and return the product of the two numbers which will also be int"""
    return a*b

print(multiply.invoke({'a': 3, 'b': 4}))

print(multiply.name)
print(multiply.description)
print(multiply.args)

# tool binding
model = ChatOllama(model='llama3.1')

llm_with_tools = model.bind_tools([multiply])
print('-'*100)
print(llm_with_tools)
print('-'*100)
print(llm_with_tools.invoke('Hi, how are you?'))
result = llm_with_tools.invoke('Can you multiply 3 with 10')
print(result)
print(result.tool_calls)
print(result.tool_calls[0])

print(multiply.invoke(result.tool_calls[0]['args']))

print(multiply.invoke(result.tool_calls[0]))

# Proper Organized

query = HumanMessage('Can you multiply 3 with 1000?')
messages = [query]
print(messages)

result = llm_with_tools.invoke(messages)
print(type(result))
messages.append(result)
print(messages)

tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)
print(messages)

# By now I have HumanMessage, AIMessage and ToolMessage, now I can send this wole history to LLM and summarize
print('='*100)
print(llm_with_tools.invoke(messages).content)




