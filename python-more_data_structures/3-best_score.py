#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        scores = list(a_dictionary.values())
        max_score = max(scores)

        best = ""
        for key in a_dictionary.keys():
            if a_dictionary[key] == max_score:
                best = key
        return best
    else:
        return None
