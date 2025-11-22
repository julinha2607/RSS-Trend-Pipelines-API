#Does the analysis of what is imported, gets key-words, does the cleaning of the data

from collections import Counter
import re

def clean_text(text):
    """
    Basic text cleaning.
    """
    # Remove HTML tags (if any remain), special chars, etc.
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

def extract_keywords(text, top_n=5):
    """
    Extracts top keywords from text.
    """
    #A list of words we do not want to consider as keywords
    stop_words = set(['the', 'a', 'an', 'in', 'on', 'at', 'for', 'to', 'of', 'and', 'is', 'are', 'with', 'by', 'this', 'that', 'it', 'from', 'as'])
    #Splits the text into words
    words = clean_text(text).split()
    #Filters out stop words and short words
    filtered_words = [w for w in words if w not in stop_words and len(w) > 3]
    #Counts the frequency of each word
    return Counter(filtered_words).most_common(top_n)
