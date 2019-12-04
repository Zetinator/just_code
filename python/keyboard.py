def time_taken(keyboard, text):
    def get_distance(string, a, b):
        return abs(string.index(a) - string.index(b))
    def go_deep(keyboard, text, n, s):
        if text == '': return n
        n += get_distance(keyboard, text[0], s)
        s = text[0]
        return go_deep(keyboard, text[1:], n, s)
    return go_deep(keyboard, text, 0, keyboard[0])
    
# test
keyboard = "abcdefghijklmnopqrstuvwxy"
text = "cba"
print('testing with: {}'.format(keyboard, text))
print(time_taken(keyboard,text))
