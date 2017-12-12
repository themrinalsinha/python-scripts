#!/usr/bin/python3

"""
    Given two string, find the longest common sub-sequence
    eg:
        str1 = 'canyouseeme'
        str2 = 'noicantseeyou'
        lcs(str1, str2) = canyou
"""

def lcs(string1, string2):
    if not string1 or not string2: return ''
    s1, s1_str = string1[0], string1[1:]
    s2, s2_str = string2[0], string2[1:]
    if s1 == s2:
        return s1 + lcs(s1_str, s2_str)
    return max(lcs(string1, s2_str), lcs(s1_str, string2), key = len)

print(lcs('canyouseeme', 'noicantseeyou'))