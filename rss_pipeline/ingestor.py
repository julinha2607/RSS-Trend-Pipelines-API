#Imports the content from the websites to the database

import feedparser
#Imports the list of websites from the config file
from .config import RSS_FEEDS

def fetch_feeds():
    #This underneath is called a docstring, it is used to document the function
    """
    Fetches and parses RSS feeds.
    Returns a list of entries.
    """
    #Initializes an empty list to store the entries
    all_entries = []
    #Fetches the RSS feeds from the config file 
    for url in RSS_FEEDS:
        print(f"Fetching {url}...")
        #The variable feed is used to store the results from the parser
        feed = feedparser.parse(url)
        #Parses the RSS feeds
        for entry in feed.entries:
            # Adds source for tracking
            entry['source'] = feed.feed.title if 'title' in feed.feed else url
            # Adds the entry to the list
            all_entries.append(entry)
    
    return all_entries

if __name__ == "__main__":
    # Tests the fetcher
    entries = fetch_feeds()
    print(f"Fetched {len(entries)} articles.")
