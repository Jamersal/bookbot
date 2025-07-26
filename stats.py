def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
        return counts 

def sort_characters(counts):
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)



