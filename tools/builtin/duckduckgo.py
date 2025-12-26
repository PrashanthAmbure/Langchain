from langchain_community.tools import DuckDuckGoSearchRun


search_tool = DuckDuckGoSearchRun()

# result = search_tool.invoke('ipl news')
# result = search_tool.invoke('top news in india')
result = search_tool.invoke('latest sensex points in india')

print(f"Result: {result}")