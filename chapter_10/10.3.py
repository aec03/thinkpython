# cumulative sum of list

def cum_sum(l):
    for x in range(len(l)):
        if x == 0:
            continue
        l[x] = l[x - 1] + l[x]
        
    return l

# print cummative-sum function
print(cum_sum([1, 2, 3, 4, 5, 6]))