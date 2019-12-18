"""https://www.hackerrank.com/challenges/minimum-time-required/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

You are planning production for an order. You have a number of machines that each have a fixed number of days to produce an item. Given that all the machines operate simultaneously, determine the minimum number of days to produce the required order.

Complete the minimumTime function in the editor below. It should return an integer representing the minimum number of days required to complete the order.

minimumTime has the following parameter(s):

machines: an array of integers representing days to produce one item per machine
goal: an integer, the number of items required to complete the order
"""

def minTime(machines, goal):
    """linear solution, too slow... for hackerrank
    """
    products, days = 0, 0
    while products < goal:
        days += 1
        products += [days%machine for machine in machines].count(0)
    return days

def minTime(machines, goal):
    """nonlinear solution, get the LCM
    problem: -6.000000000000001 -> 7
    fucking floating point arithmetics... going to integer arithmetic
    almost... still runtime error
    """
    # get the cumulative product of the machines
    acc = 1
    for e in machines:
        acc *= e
    # execute goal/(products per day) but in integer arithmetics
    days = (-goal*acc)//sum([acc//machine for machine in machines])
    return int(-days)

def minTime(machines, goal):
    """fixed floating point arithmetics with rounding
    still not working... we cannot take 2 half finished products and count as 1 finished
    """
    ans = (goal/one_daywork)
    if (round(ans, 6)).is_integer():
        return int(ans)
    else:
        return (int(math.ceil(ans)))

def minTime(machines, goal):
    """binary search approach
    success...
    """
    # get search bounds
    minima, maxima = float('inf'), -float('inf')
    for e in machines:
        if e < minima: minima = e
        if e > maxima: maxima = e
    l = goal/len(machines) * minima  # what if all the machines were fast
    r = goal/len(machines) * maxima  # what if all were slow
    # standard binary search
    while l < r:
        m = (l+r)//2
        if sum(m//e for e in machines) < goal:
            l = m+1
        else:
            r = m
    return int(l)

# test
machines = [4,5,6]
goal = 12
machines = [1,3,4]
goal = 10
machines = [2,3]
goal = 5
print(f'testing with: {machines}')
print(f'ans: {minTime(machines, goal)}')
