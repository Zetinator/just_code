def count_colitions(S,E):
    persons = get_ranges(S,E)
    colitions = 0
    for hour in range(min(S),max(E)+1):
        colitions_hour = 0
        for i,e in enumerate(S):
            for hour_person in range(S[i],E[i]+1):
                if hour_person == hour:
                    colitions_hour += 1
        print('STATUS: hour: {}, colitions: {}'.format(hour, colitions_hour))
        colitions = max(colitions, colitions_hour)
    return colitions

# test
S = [1, 2, 6, 5, 3]
E = [5, 5, 7, 6, 8]
print('testing with: S:{}, E:{}'.format(S,E))
print('total_colitions: {}'.format(count_colitions(S,E)))
