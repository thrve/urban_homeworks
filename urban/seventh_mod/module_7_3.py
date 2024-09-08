#!/usr/bin/env python


import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = re.sub(r'[,\.\=\!\?\;\:\-]', '', line).lower()
                    words.extend(line.split())
            all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            try:
                index = words.index(word)
                result[file_name] = index + 1
            except ValueError:
                pass
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result
