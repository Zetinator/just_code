def bubble(x):
    swap = True
    while swap:
        print('STATE: {}'.format(x))
        swap = False
        for i, e in enumerate(x[:-1]):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i] 
                swap = True
    return x

# test
test = [1, 3, 2, 6, 5, 2, 5,]
print('testing with: {}'.format(test))
print('ANS: {}'.format(bubble(test)))

        
