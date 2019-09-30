def k_closest(points, K):
    ans = []
    def get_distance(points):
        d = [(d[0]**2+d[1]**2)**(1/2) for d in points]
        return d
    d = get_distance(points)
    for i in range(K):
        index = d.index(min(d))
        d.pop(index)
        ans.append(points.pop(index))
    return ans

# test
points = [[1,3],[-2,2],[8,10],[5,6],[18,13]]
K = 4
print('Testing with: points: {}, K:{}'.format(points, K))
print(k_closest(points, K))
