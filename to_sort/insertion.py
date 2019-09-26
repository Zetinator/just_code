def insertion(x):
    insertions = []
    while x:
        print('STATE: insertions:{}, x: {}'.format(insertions, x))
        for e in x:
            insertions.append(x.pop(x.index(min(x))))
    return insertions

# test
test = [1, 3, 2, 6, 5, 2, 5,]
print('testing with: {}'.format(test))
print('ANS: {}'.format(insertion(test)))

        
