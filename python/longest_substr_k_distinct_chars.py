# Given a string, find the length of the longest substring with at most x distinct characters.

# aabccba   x=2  ans=4
# aabcddccacbd   x=3  ans=7

def efficient_substrings(s, x):
    list_chars = list(s)
    n = len(list_chars)
    max = 0
    start = 0
    while start < n - max:
        current_idx = start
        distinct_count = 0
        hmap = {}
        while distinct_count <= x and current_idx < n:
            if list_chars[current_idx] not in hmap:
                hmap[list_chars[current_idx]] = 'exists'
                distinct_count += 1
            if distinct_count <= x:
                current_idx += 1
        if current_idx - start > max:
            max = current_idx - start
        start += 1
    return max
