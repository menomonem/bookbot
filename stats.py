def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_of_char(text):
    elements = {}
    lower_case = text.lower()
    for char in lower_case:
        if char not in elements:
            elements[char] = 1
        else:
            elements[char] += 1
    return elements

def sort_dict(d):
    l=[]
    for e in d:
        l.append({"char": e, "num": d[e]})
        l.sort(reverse=True, key=lambda x: x["num"])
    return l