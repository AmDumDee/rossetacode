def bwt(s):
    """Apply Burrows-Wheeler transform to input string."""
    assert "\002" not in s and "\003" not in s, "Input string cannot contain STX and ETX characters"
    s = "\002" + s + "\003"  
    table = sorted(s[i:] + s[:i] for i in range(len(s)))  
    last_column = [row[-1:] for row in table]  
    return "".join(last_column)  


def ibwt(r):
    """Apply inverse Burrows-Wheeler transform."""
    table = [""] * len(r)  
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  
    s = [row for row in table if row.endswith("\003")][0]  
    return s.rstrip("\003").strip("\002")  
