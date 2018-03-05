''' The function should return true if a pair in data adds up to the sum.
'''
def has_pair_with_sum(data, sum):
    comps = [] # Complements
    for value in data:
        if value in comps: # If complements contains the value, means that a pair adds up to the sum
            return True
        comps.append(sum-value) # Store the complement
    return False