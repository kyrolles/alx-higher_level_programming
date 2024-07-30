#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or a_dictionary == {}:
        return None
    best_key = list(a_dictionary.keys())[0]
    best_value = a_dictionary[best_key]

    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key
    return best_key



a_dictionary = {}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))