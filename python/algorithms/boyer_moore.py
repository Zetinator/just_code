"""
return the index of the first occurence of the pattern in the text
implementation of the boyer moore horspool algorithm
"""

def pre_process(pattern):
    """populate skip dictionary
    on a missmatch we can skip up to the next appearance of the letter in the word
    this skips is what makes boyer-moore so efficient
    """
    skip_dict = {letter:len(pattern)-1 - i for i, letter in enumerate(pattern)}
    return skip_dict

def boyer_moore(pattern: str, text: str) -> int:
    """finds the first perfect match of the pattern in the text
    """
    if len(pattern) > len(text): raise ValueError(f'{pattern} not found')
    skip_dict = pre_process(pattern)
    skip = 0
    while len(text) - skip > len(pattern):
        # navigate the pattern from right to left
        for i in reversed(range(len(pattern))):  
            # on perfect match
            if i == 0 and text[skip + i] == pattern[i]: return skip
            # on missmatch
            if text[skip + i] != pattern[i]:
                # we skip until the next appearance of the letter in the pattern
                skip += skip_dict.get(text[skip + i], len(pattern))
                break
    raise ValueError(f'{pattern} not found')
