import json

from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
import requests

API_KEY=""
# Create tool
@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    This function fetches the currency conversion factor between a given base currency and target currency
    :param base_currency:
    :param target_currency:
    :return:
    """
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    return response.json()

@tool
def convert(base_currency_value: int, conversion_rate: float)-> float:
    """
    given a currency conversion rate this function calcs the target currency value from a given base currency value
    :param base_currency_value:
    :param conversion_rate:
    :return:
    """
    return base_currency_value * conversion_rate


# Tool Binding
llm = ChatOllama(model='llama3.1')
llm_with_tool = llm.bind_tools([get_conversion_factor, convert])

messages = [HumanMessage('What is the conversion factor between USD and INR? Based on that can you convert 10 USD to INR?')]

ai_message = llm_with_tool.invoke(messages)

messages.append(ai_message)

print(messages)

for tool_call in ai_message.tool_calls:
    # Execute the first tool and get the conversion rate
    if tool_call['name'] == 'get_conversion_factor':
        tool1_message = get_conversion_factor.invoke(tool_call)
        print(tool1_message)
        messages.append(tool1_message)
        # fetch the conversion rate
        conversion_rate = json.loads(tool1_message.content)['conversion_rate']
    # Execute the second tool using the conversion rate from first tool
    if tool_call['name'] == 'convert':
        tool_call['args']['conversion_rate']=conversion_rate
        tool2_message = convert.invoke(tool_call)
        messages.append(tool2_message)

print('*'*100)
print(messages)
print(llm_with_tool.invoke(messages).content)



