"""
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_r=internal-search
"""

def sherlockAndAnagrams(s):
    sets = []
    s_counter = Counter()
    for i,_ in enumerate(s):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if Counter(substring) in sets:
                index = sets.index(Counter(substring))
                s_counter[index] += 1
                print(f's: {s[i:j+1]} is in')
            else:
                print(f'adding {s[i:j+1]} to sets: {sets}')
                sets.append(Counter(substring))
        print(f's_counter: {s_counter}')
        acc = 0
        for e in s_counter.values():
            acc += math.factorial(e+1) // (2*math.factorial(e-1))
    return acc

