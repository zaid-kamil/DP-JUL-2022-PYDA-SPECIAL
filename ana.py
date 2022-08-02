def stringAnagram(dictionary, query):
    out = []
    for word in query:
        count = 0
        for word2 in dictionary:
            if len(word) == len(word2):
                if sorted(word) == sorted(word2):
                    count+=1
        out.append(count)
    return out

dictionary = [
    'heater',
    'cold',
    'clod',
    'reheat',
    'docl',
]
query = [
    'codl',
    'heater',
    'abcd'
]
result = stringAnagram(dictionary, query)
print(result)