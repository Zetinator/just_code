"""
recursive insertion sort
"""
def r_insertion(x):
    def divide(x, ans):
        # print(f'STATUS: x:{x}, ans:{ans}')
        if not x: return ans
        if not ans: return divide(x[1:],[x[0]])
        for i in range(len(ans)):
            if x[0] < ans[i]:
                ans.insert(i,x[0])
                return divide(x[1:], ans)
        ans.insert(len(ans), x[0])
        return divide(x[1:], ans)
    return divide(x, [])

# test
# test = [12, 11, 13, 5, 6]
test = [1, 3, 2, 6, 5, 2, 5, 0]
print(f'testing with: {test}')
print(f'ANS: {r_insertion(test)}')
