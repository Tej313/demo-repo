def count_characters(s):
    """
    Counts the number of times each character appears in a string.
    
    :param s: str - the string to count characters in
    :return: dict - a dictionary of characters and their counts
    """
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        # Printing the count of each character
    for char, count in char_count.items():
        print(f"'{char}' occurs {count} times.")
    return char_count