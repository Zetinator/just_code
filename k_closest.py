def k_closest(points, K):
    return sorted(points, key=lambda d: ((d[0])**2+(d[1])**2)**(1/2))[:K]

# test
points = [[1,3],[-2,2],[8,10],[5,6],[18,13],[20,40]]
K = 4
print('Testing with: points: {}, K:{}'.format(points, K))
print(k_closest(points, K))
