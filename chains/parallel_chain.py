from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

llama_model = ChatOllama(model="llama3.1")
mistral_model = ChatOllama(model="mistral")

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text - \n {text}',
    input_variables=['text'],
    validate_template=True
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text- \n {text}',
    input_variables=['text'],
    validate_template=True
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz - {quiz}',
    input_variables=['notes', 'quiz'],
    validate_template=True
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | llama_model | parser,
    'quiz': prompt2 | mistral_model | parser
})

merge_chain = prompt3 | llama_model | parser

chain = parallel_chain | merge_chain

text = """
Cricket is a popular bat-and-ball game played between two teams of eleven players each, primarily in Commonwealth nations. The game is centered on a large oval or circular field, with a rectangular 22-yard-long pitch in the middle.
The objective is for one team to bat and score as many runs as possible, while the opposing team fields and bowls to dismiss the batsmen. The game is divided into sections called innings, where the teams alternate between batting and fielding. A designated bowler delivers the ball toward a set of three wooden stumps topped with two bails, called a wicket, at one end of the pitch, in front of which stands a batsman. The batsman's goal is to prevent the ball from hitting the wicket and to hit the ball to score runs.
Runs are primarily scored in two ways:
Running between the wickets after hitting the ball into the field of play.
Hitting the ball to or over the boundary for a fixed number of runs (four or six).
The sport is known for its various formats, from the multi-day Test cricket—considered the highest standard of the game—to one-day matches and the fast-paced Twenty20. Beyond its technicalities, cricket is celebrated for its emphasis on teamwork, discipline, and the thrilling competition it provides for players and fans alike.
"""
response = chain.invoke({'text': text})

print(response)

print(chain.get_graph().draw_ascii())

