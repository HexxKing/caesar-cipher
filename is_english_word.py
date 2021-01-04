# serves as our "dictionary", aka a corpus (nltk)
# poetry add nltk

from corpus_loader import word_list, name_list
import re

candidates = [
  "a dark and stormy night"
  "once upon a time"
  "I like it, I want it, I got it, I have it"
]

def count_words(text):

  candidate_words = text.split()

  word_count = 0

  for candidate in candidates:
    potenital_word = re.sub(r'[^A-Za-z]+', '', candidate)

    if potenital_word.lower() in word_list or potenital_word in name_list:
      word_count += 1

  return word_count


for phrase in candidates:
    word_count = count_words(phrase)
    percentage = int(word_count / len(phrase.split()) * 100)
    if percentage > 50:
        print(phrase, percentage)