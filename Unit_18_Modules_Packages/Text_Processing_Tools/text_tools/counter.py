# counter.py
def count_words(text):
    """Count the number of words in the text"""
    return len(text.split())

def count_characters(text):
    """Count the number of characters in the text"""
    return len(text)

def count_sentences(text):
    """Count sentences based on '.' split"""
    return len([s for s in text.split('.') if s.strip()])