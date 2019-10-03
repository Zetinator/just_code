from functools import lru_cache
@lru_cache(maxsize=512)
def go_deep(v, w, c_value, c_capacity):
    if not w: return c_value
    i_value = v[0]
    i_weight = w[0]
    if c_capacity - i_weight < 0:
        return go_deep(v[1:], w[1:],c_value, c_capacity)
    return max(go_deep(v[1:], w[1:], c_value+i_value, c_capacity-i_weight),
            go_deep(v[1:], w[1:], c_value, c_capacity))
def knapsack(v,w,W):
    return go_deep(v,w, 0, W)

# test
v = (60,100,120,500)
w = (10,20,30,50)
W = 50
print('testing with: v:{}, w:{}, W:{}'.format(v, w, W))
print(knapsack(v,w,W))
