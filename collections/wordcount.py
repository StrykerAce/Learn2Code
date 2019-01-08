# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.
def word_count(str):
    words = str.lower().split()
    results = {}
    for word in words:
        count = 0
        for w in words:
            if word == w:
                count += 1
        results[word] = count
    print(results)
    
    
word_count("I do not like it Sam I Am")
word_count("How much wood could a wood chuck wood if a wood chuck could chuck wood")
