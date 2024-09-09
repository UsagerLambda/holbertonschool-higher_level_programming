#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    
    best_score = 0
    best_player = None

    for player, score in a_dictionary.items():
        if score > best_score:
            best_score = score
            best_player = player

    return best_player
