def merge(x):
    def divide(x):
        if len(x) == 1: return x
        # divide
        x, y = divide(x[:int(len(x)/2)]), divide(x[int(len(x)/2):])
        # conquer
        ans = []
        while y and x:
            if x[0] < y[0]:
                ans.append(x.pop(0))
            else:
                ans.append(y.pop(0))
        while x:
            ans.append(x.pop(0))
        while y:
            ans.append(y.pop(0))
        print('MERGE: {}'.format(ans))
        return ans
    return divide(x)

# test
test = [1, 3, 2, 6, 5, 2, 5, 0]
print('testing with: {}'.format(test))
print('ANS: {}'.format(merge(test)))
