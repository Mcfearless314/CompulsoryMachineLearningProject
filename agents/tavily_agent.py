from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')


tavily_client = TavilyClient(api_key)

tavily_search = ""
tavily_response = ""


def get_user_input():
    # Ask the user for each part of the query
    topic = input("Enter the topic of the research paper: ")
    year_condition = input("Would you like the paper to be published in, before, or after a certain year? (in/before/after): ").lower()
    year = input("Enter the year: ")
    citations = input("Enter the minimum number of citations: ")
    create_query(topic,year_condition,year, citations)


def create_query(topic, year_condition, year, citations):
    # Create a query string based on the user's inputs
    global tavily_search
    tavily_search = (
        f"Find peer-reviewed academic journal articles on {topic}, "
        f"published {year_condition} {year}, with at least {citations} citations. "
        f"Exclude search engines or indexing pages like Google Scholar, Semantic Scholar, and citation directories. "
        f"Include links to full papers or abstracts from trusted academic sources like PubMed, ScienceDirect, JSTOR, Springer, or Wiley."
    )
    global tavily_response
    tavily_response = tavily_client.search(tavily_search)

    print(f"\nSearch results for: '{tavily_search}'\n")

    if "results" in tavily_response and tavily_response["results"]:
        results = tavily_response["results"]
        for i, result in enumerate(results, start=1):
            title = result.get('title', 'No title available')
            url = result.get('url', 'No link available')
            content = result.get('content', 'No content available')

            print(f"Paper #{i}: '{title}'")
            print(f"Link: {url}")
            print(f"Description: {content}\n")
    else:
        print("No results found.")


