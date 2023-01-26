import requests
import random
import os
import optparse

def generate_comment(name_list, path_to_wordlist):
    comments = {}
    all_words = open(path_to_wordlist, 'r')
    all_words = all_words.read().strip(' ')
    print(all_words)


generate_comment(0, 'comments.txt')