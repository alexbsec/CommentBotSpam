import requests
import random
import os
import optparse
from time import sleep


def generate_comments_by_name(path_to_name_list, path_to_wordlist):
    comments = {}
    all_words = open(path_to_wordlist, 'r')
    all_words = all_words.read().strip(' ')

    all_names = open(path_to_name_list, 'r')
    all_names = all_names.read().strip(' ')

    negative = "não"
    verbs = ["gostei", "amei", "achei", "me interessei", "tive", "nunca vi", "nunca encontrei"]
    starting_verbs = ["Gostei", "Amei", "Achei", "Me interessei", "Tive", "Nunca vi", "Nunca encontrei"]
    simple_phrase = ["Massa", "Curti", "Top", "Legal", "Bom", "Muito bom", "Bom"]
    space = " "
    starting = "Eu"
    start = starting[random.randint(0, len(starting)-1)]
    
    for name in all_names:
        how_many_words = random.randint(0, 6)
        if how_many_words == 1:
            phrase = simple_phrase[random.randint(0, len(simple_phrase)-1)]
        elif how_many_words == 2:
            phrase 
        else:
            verb = verbs[random.randint(0, len(verbs)-1)]
            start = 'Eu'
            phrase = start + space + verb

        print(phrase)
