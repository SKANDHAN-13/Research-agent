from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)



search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="duckduckgo_web_search",
    func=search.run,
    description="Performs a DuckDuckGo web search and returns concise results for a given query.",
)

api_wrapper = WikipediaAPIWrapper(doc_content_chars_max=200)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

wiki_tool = Tool(
    name="condensed_wikipedia_lookup",
    func=wiki_tool.run,
    description="Fetches and returns a brief summary of a topic using Wikipedia (max 200 characters).",
)