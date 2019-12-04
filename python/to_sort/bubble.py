def bubble(x):
    swap = True
    while swap:
        print('STATE: {}'.format(x))
        swap = False
        to_sort = 1
        for i, e in enumerate(x[:-to_sort]):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i] 
                to_sort += 1
                swap = True
    return x

# test
test = [1, 3, 2, 6, 5, 2, 5,]
print('testing with: {}'.format(test))
print('ANS: {}'.format(bubble(test)))

        
