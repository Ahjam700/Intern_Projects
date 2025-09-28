#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from collections import Counter

def get_content(Ozone_layer):
    """
    Fetch the content of a Wikipedia article using the Wikipedia API.
    
    Parameters:
    - article_name (str): The name of the article to fetch.
    
    Returns:
    - dict: A dictionary containing metadata and article content.
    """
    # Wikipedia API endpoint
    url = "https://en.wikipedia.org/w/api.php"
    
    # Parameters for the API request
    params = {
        "action": "query",
        "format": "json",
        "titles": Ozone_layer,
        "prop": "revisions",
        "rvslots": "main",
        "rvprop": "content",
    }
    
    # Send the request to the Wikipedia API
    response = requests.get(url, params=params)
    data = response.json()
    
    return data

def merge_contents(data, splitters=[" ", "\n"]):
    """
    Extract, clean, and split the content from the Wikipedia API response using the splitter characters.
    
    Parameters:
    - data (dict): The API response containing article content.
    - splitters (list): A list of characters used to split the content into words (default: space and newline).
    
    Returns:
    - str: A cleaned and split string containing the article content.
    """
    # Extracting content from the API response
    try:
        pages = data['query']['pages']
        page_content = next(iter(pages.values()))  # Get the first page from the response
        revisions = page_content['revisions']
        content = revisions[0]['slots']['main']['content']
        
        # Clean and simplify the content (remove unnecessary parts)
        content = content.replace("{{pp-semi-indef}}", "").strip()  # Removing template
        
        # Process the content repeatedly with the splitters
        index = 0  # Counter for tracking splitters
        while index < len(splitters):
            splitter = splitters[index]
            content = content.replace(splitter, " ")  # Replace each splitter with a space
            index += 1  # Move to the next splitter
        
        # Return a portion of the content after splitting (for readability)
        content = content[:500]  # Limit to the first 500 characters for display
        
        return content
    except KeyError:
        return "Content not available or error in the response."

def tokenize(content):
    """
    Tokenize the content into individual words (or tokens) based on a set of delimiters.
    
    Parameters:
    - content (str): The content to tokenize.
    
    Returns:
    - list: A list of tokens (words).
    """
    # Define the delimiters we want to use for tokenization (e.g., spaces, newlines, punctuation)
    splitters = [" ", "\n", ".", ",", "!", "?", "(", ")", "[", "]", "{", "}", ";", ":", "-", "_", "'", "\""]
    
    # Replace the delimiters with spaces
    for splitter in splitters:
        content = content.replace(splitter, " ")
    
    # Tokenize by splitting the content into words based on spaces
    tokens = content.split()
    
    return tokens

def lower_collection(collection):
    """
    Convert all tokens in the collection to lowercase.
    
    Parameters:
    - collection (list): A list of tokens (words).
    
    Returns:
    - list: A list of tokens in lowercase.
    """
    # Convert each token in the collection to lowercase
    return [token.lower() for token in collection]

def count_frequency(collection):
    """
    Count the frequency of each token in the collection.
    
    Parameters:
    - collection (list): A list of tokens (words).
    
    Returns:
    - Counter: A dictionary-like object containing token frequencies.
    """
    # Use Counter from collections to count token frequencies
    return Counter(collection)

def print_most_frequent(frequencies, n):
    """
    Print the `n` most frequent tokens and their counts.
    
    Parameters:
    - frequencies (Counter): A dictionary-like object containing token frequencies.
    - n (int): The number of most frequent tokens to display.
    """
    # Get the most common `n` items from the frequency Counter
    most_common = frequencies.most_common(n)
    
    # Print the most frequent tokens and their frequencies
    for token, freq in most_common:
        print(f"{token}: {freq}")

def remove_stop_words(words, stop_words):
    """
    Remove stop words from the list of words.
    
    Parameters:
    - words (list): A list of tokens (words).
    - stop_words (list): A list of stop words to be removed.
    
    Returns:
    - list: A filtered list of tokens with stop words removed.
    """
    # Filter out any word that is in the stop_words list
    return [word for word in words if word not in stop_words]

# Main part of the script
article_name = "Ozone_layer"
stop_words = ["the", "a", "of", "to", "in", "about", "and", "that", "for", "is", "on", "it", "as", "with", "an", "at", "by"]

data = get_content(article_name)
merged_content = merge_contents(data)

# Tokenize the merged content
collection = tokenize(merged_content)

# Convert all tokens to lowercase
lowered_collection = lower_collection(collection)

# Remove stop words from the collection
filtered_collection = remove_stop_words(lowered_collection, stop_words)

# Count the frequency of each token in the filtered collection
frequencies = count_frequency(filtered_collection)

# Print the 10 most frequent tokens
print_most_frequent(frequencies, 10)


# In[ ]:




