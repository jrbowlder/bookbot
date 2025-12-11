def word_count(text):
    number_of_words = text.split()
    return len(number_of_words)

def char_count(text):
    counts={}

    for char in text:
        char = char.lower()

        if char not in counts:
            counts[char] = 0
        
        counts[char] += 1

    return counts

def sort_on(dictionary):
    return dictionary["num"]

def sort_dict(counts):
    sorted_list = []
    
    for ch in counts:
        sorted_list.append({"char": ch, "num": counts[ch]})
        
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list 

