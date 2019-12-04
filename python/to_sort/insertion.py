def insertion(x):
    for i, e in enumerate(x):
        print(f'STATE: x:{x}, index:{i}, current_element:{e}')
        for j in reversed(range(i)):
            if e >= x[j]: break
            x[j+1], x[j] = x[j], x[j+1]
    return x

# test
test = [1, 3, 2, 6, 5, 2, 5,]
print('testing with: {}'.format(test))
print('ANS: {}'.format(insertion(test)))

        
