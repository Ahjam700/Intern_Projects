def my_levenshtein(str1, str2):
    if len(str1) != len(str2):
        return -1

    difference_count = 0

    for char1, char2 in zip(str1, str2):

        if char1 != char2:
            difference_count += 1
    return difference_count