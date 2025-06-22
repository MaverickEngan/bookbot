def get_num_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def count_characters(text):
    list_of_characters = {}
    temp_char = ""
    for char in text:
        temp_char = char.lower()
        if temp_char in list_of_characters:
            list_of_characters[temp_char] += 1
        else:
            list_of_characters[temp_char] = 1
    return list_of_characters

def sort_on(counts):
    return counts["num"]

def sort_characters(char_count):
    sorted_characters = []
    for char in char_count:
        sorted_characters.append({"char": char, "num": char_count[char]})
    sorted_characters.sort(key=sort_on, reverse=True)
    return sorted_characters