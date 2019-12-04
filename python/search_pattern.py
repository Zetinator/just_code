"""
return the index of the first occurence of the pattern in the text
implementation of the boyer moore horspool algorithm
"""
def pre_process(pattern):
    # populate skip dictionary
    skip_dict = {letter:len(pattern)-1 - i for i, letter in enumerate(pattern)}
    return skip_dict

def search(pattern, text):
    # save of some time...
    if len(pattern) > len(text): raise ValueError(f'{pattern} not found')
    skip_dict = pre_process(pattern)
    skip = 0
    while len(text) - skip > len(pattern):
        for i in reversed(range(len(pattern))):  # navigate the pattern from right to left
            print(f'comparing: pattern: {pattern[i]}, text: {text[skip + i]}')
            # case: all letters match
            if i == 0 and text[skip + i] == pattern[i]: return skip
            # case: missmatch
            if text[skip + i] != pattern[i]:
                print(f'missmatch skipping --> {skip_dict.get(text[skip + i], len(pattern))}')
                skip += skip_dict.get(text[skip + i], len(pattern))  # how much can we skip
                break
    # raise error if not found
    raise ValueError(f'{pattern} not found')

if __name__ == '__main__':
    pattern = 'marion'
    text = "erick quiere a marion, aunque marion ya no nos hable :("
    print(f'ANS: {search(pattern, text)}')
