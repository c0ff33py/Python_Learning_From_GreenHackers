# main.py
from text_tools import to_upper, count_words, title_case, count_sentences,to_lower, count_characters

sample_text = "hello world. python is amazing."

# Use formatter functions
print(to_upper(sample_text))
print(title_case(sample_text))
print(to_lower(sample_text))

# Use counter funcitons
print("Sentences Count: ",count_sentences(sample_text))
print("Word count: ",count_words(sample_text))
print("Characters count: ",count_characters(sample_text))