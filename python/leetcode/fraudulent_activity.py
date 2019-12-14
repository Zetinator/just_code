"""https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting

HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
"""

def get_median(x):
    x = sorted(x)
    m = len(x)//2
    return (x[m]+x[m+1])/2 if len(x)%2 == 0 else x[m]

def activityNotifications(expenditure, d):
    # special case: n < d
    if len(expenditure) < d: return 0
    # general case
    notifications = 0
    for i in range(d, len(expenditure)):
        c_history = expenditure[i-d:i]
        print(f'history: {c_history}, median: {get_median(c_history)}, next: {expenditure[i]}')
        if expenditure[i] >= 2*get_median(c_history): notifications += 1
    return notifications

# the code is not executing between the time limits

def get_median(v, d):
    m = d//2+1
    i, counter = 0, 0
    c_median = 0
    while counter < m:
        prev_median, c_median = c_median, i
        for e in range(v[i]):
            counter += 1
            print(f'prev: {prev_median}, current_median: {c_median}, counter: {counter}, m: {m}')
            if counter == m: break
        i += 1
    return c_median if d%2 == 1 else (prev_median+c_median)/2


def activityNotifications(expenditure, d):
    # special case: n < d
    if len(expenditure) < d: return 0
    v = [0]*201
    # push first d elements
    for e in expenditure[:d]:
        v[e] += 1
    notifications = 0
    for i in range(d, len(expenditure)):
        # compare current element with the current median
        median = get_median(v, d)
        print(f'median: {median}, next: {expenditure[i]}')
        if expenditure[i] >= 2*median: notifications += 1
        # push new expenditure[i]
        v[expenditure[i]] += 1
        # pop oldest element
        v[expenditure[i-d]] -= 1
    return notifications


# test
test = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 4
print(f'testing with: {test}')
print(f'ans: {activityNotifications(test, d)}')
