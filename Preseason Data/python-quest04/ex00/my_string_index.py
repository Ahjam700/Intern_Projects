def my_string_index(haystack, needle):
    # Check if the needle is a single character
    if len(needle) != 1:
        return -1  # Return -1 if needle is not a single character
    
    # Find the index of the first occurrence of needle in haystack
    index = haystack.find(needle)
    
    return index


