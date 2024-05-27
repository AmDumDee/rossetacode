
from typing import List

ALPHABET_SIZE = 256

def alphabet_index(c: str) -> int:
    
    val = ord(c)
    assert 0 <= val < ALPHABET_SIZE
    return val

def match_length(S: str, idx1: int, idx2: int) -> int:
    
    if idx1 == idx2:
        return len(S) - idx1
    match_count = 0
    while idx1 < len(S) and idx2 < len(S) and S[idx1] == S[idx2]:
        match_count += 1
        idx1 += 1
        idx2 += 1
    return match_count

def fundamental_preprocess(S: str) -> List[int]:
    
    if len(S) == 0:  
        return []
    if len(S) == 1:  
        return [1]
    z = [0 for x in S]
    z[0] = len(S)
    z[1] = match_length(S, 0, 1)
    for i in range(2, 1 + z[1]):  
        z[i] = z[1] - i + 1
    
    l = 0
    r = 0
    for i in range(2 + z[1], len(S)):
        if i <= r:  
            k = i - l
            b = z[k]
            a = r - i + 1
            if b < a:  
                z[i] = b
            else:  
                z[i] = a + match_length(S, a, r + 1)
                l = i
                r = i + z[i] - 1
        else:  
            z[i] = match_length(S, 0, i)
            if z[i] > 0:
                l = i
                r = i + z[i] - 1
    return z

def bad_character_table(S: str) -> List[List[int]]:
    
    if len(S) == 0:
        return [[] for a in range(ALPHABET_SIZE)]
    R = [[-1] for a in range(ALPHABET_SIZE)]
    alpha = [-1 for a in range(ALPHABET_SIZE)]
    for i, c in enumerate(S):
        alpha[alphabet_index(c)] = i
        for j, a in enumerate(alpha):
            R[j].append(a)
    return R

def good_suffix_table(S: str) -> List[int]:
    
    L = [-1 for c in S]
    N = fundamental_preprocess(S[::-1])  
    N.reverse()
    for j in range(0, len(S) - 1):
        i = len(S) - N[j]
        if i != len(S):
            L[i] = j
    return L

def full_shift_table(S: str) -> List[int]:
    
    F = [0 for c in S]
    Z = fundamental_preprocess(S)
    longest = 0
    for i, zv in enumerate(reversed(Z)):
        longest = max(zv, longest) if zv == i + 1 else longest
        F[-i - 1] = longest
    return F

def string_search(P, T) -> List[int]:
    
    if len(P) == 0 or len(T) == 0 or len(T) < len(P):
        return []

    matches = []

    
    R = bad_character_table(P)
    L = good_suffix_table(P)
    F = full_shift_table(P)

    k = len(P) - 1      
    previous_k = -1     
    while k < len(T):
        i = len(P) - 1  
        h = k           
        while i >= 0 and h > previous_k and P[i] == T[h]:  
            i -= 1
            h -= 1
        if i == -1 or h == previous_k:  
            matches.append(k - len(P) + 1)
            k += len(P) - F[1] if len(P) > 1 else 1
        else:  
            char_shift = i - R[alphabet_index(T[h])][i]
            if i + 1 == len(P):  
                suffix_shift = 1
            elif L[i + 1] == -1:  
                suffix_shift = len(P) - F[i + 1]
            else:               
                suffix_shift = len(P) - 1 - L[i + 1]
            shift = max(char_shift, suffix_shift)
            previous_k = k if shift >= i + 1 else previous_k  
            k += shift
    return matches

TEXT1 = 'InhisbookseriesTheArtofComputerProgrammingpublishedbyAddisonWesleyDKnuthusesanimaginarycomputertheMIXanditsassociatedmachinecodeandassemblylanguagestoillustratetheconceptsandalgorithmsastheyarepresented'
TEXT2 = "Nearby farms grew a half acre of alfalfa on the dairy's behalf, with bales of all that alfalfa exchanged for milk."
PAT1, PAT2, PAT3 = 'put', 'and', 'alfalfa'

print("Found", PAT1, "at:", string_search(PAT1, TEXT1))
print("Found", PAT2, "at:", string_search(PAT2, TEXT1))
print("Found", PAT3, "at:", string_search(PAT3, TEXT2))
