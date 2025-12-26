from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatOllama(model="llama3")
# chat_history = []
# chat_history = [
#     SystemMessage(content="You are a helpful AI assistant")
# ]

while True:
    user_input = input("You: ")
    # chat_history.append(user_input)
    # chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    # result = model.invoke(chat_history)
    # chat_history.append(result.content)
    # chat_history.append(AIMessage(content=result.content))
    print(f"AI: {result.content}")

# print(chat_history)


# Output 1: If you look at the below output, it is evident that it doesn't remember the history, hence when you uncomment Line #4, 8, 12, 13 and 16, you will see the Output 2 below
# You: Hi
# AI: Hello! It's nice to meet you. Is there something I can help you with, or would you like to chat?
# You: Which one is greater 2 or 4
# AI: That's an easy one!
#
# 4 is greater than 2.
# You: Now multiply the bigger number with 10
# AI: There is no bigger number mentioned earlier in our conversation. Could you please clarify which number you would like me to multiply by 10?
# You: exit


# Output 2: Now this also has its own draw back, when you look at the last message we do not know which was Ai message and which was user message.
# You: Hi
# AI: Hi! It's nice to meet you. Is there something I can help you with, or would you like to chat?
# You: Which one is greater 2 or 4
# AI: Nice to meet you too!
#
# As for your question, the answer is definitely 4! Two is less than four.
#
# But hey, I'm happy to chat with you about anything that's on your mind. Is there a particular topic you'd like to discuss? Or we could play a game, or generate some fun conversation starters together?
# You: Now multiply the bigger number with 10
# AI: Nice to meet you too!
#
# Ahah, good job on answering my question correctly! The bigger number is indeed 4, and multiplying it by 10 gives us... (drumroll) ...40!
#
# So, what do you say? Are you up for some fun conversation or a game? Or maybe we can generate some topics to discuss? Let me know, and I'll do my best to make our chat enjoyable!
# You: exit
# ['Hi', "Hi! It's nice to meet you. Is there something I can help you with, or would you like to chat?", 'Which one is greater 2 or 4', "Nice to meet you too!\n\nAs for your question, the answer is definitely 4! Two is less than four.\n\nBut hey, I'm happy to chat with you about anything that's on your mind. Is there a particular topic you'd like to discuss? Or we could play a game, or generate some fun conversation starters together?", 'Now multiply the bigger number with 10', "Nice to meet you too!\n\nAhah, good job on answering my question correctly! The bigger number is indeed 4, and multiplying it by 10 gives us... (drumroll) ...40!\n\nSo, what do you say? Are you up for some fun conversation or a game? Or maybe we can generate some topics to discuss? Let me know, and I'll do my best to make our chat enjoyable!", 'exit']



# Output #3:
# You: Hi
# AI: Hello! It's nice to meet you. Is there something I can help you with, or would you like to chat? I'm here to assist you with any questions, tasks, or topics you'd like to discuss. Let me know how I can be helpful today!
# You: Which one is greater 2 or 4
# AI: That's an easy one!
#
# The answer is: 4 is greater than 2.
#
# Let me know if you have any other questions or if there's anything else I can help with!
# You: Now multiply the bigger number with 10
# AI: Easy peasy!
#
# Since we established that 4 is greater, let's multiply it by 10:
#
# 4 × 10 = 40
#
# Let me know what's next!
# You: exit
# [SystemMessage(content='You are a helpful AI assistant', additional_kwargs={}, response_metadata={}), HumanMessage(content='Hi', additional_kwargs={}, response_metadata={}), AIMessage(content="Hello! It's nice to meet you. Is there something I can help you with, or would you like to chat? I'm here to assist you with any questions, tasks, or topics you'd like to discuss. Let me know how I can be helpful today!", additional_kwargs={}, response_metadata={}), HumanMessage(content='Which one is greater 2 or 4', additional_kwargs={}, response_metadata={}), AIMessage(content="That's an easy one!\n\nThe answer is: 4 is greater than 2.\n\nLet me know if you have any other questions or if there's anything else I can help with!", additional_kwargs={}, response_metadata={}), HumanMessage(content='Now multiply the bigger number with 10', additional_kwargs={}, response_metadata={}), AIMessage(content="Easy peasy!\n\nSince we established that 4 is greater, let's multiply it by 10:\n\n4 × 10 = 40\n\nLet me know what's next!", additional_kwargs={}, response_metadata={}), HumanMessage(content='exit', additional_kwargs={}, response_metadata={})]