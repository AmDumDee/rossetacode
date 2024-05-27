
def _(message):
    
    return message


def compare_and_report_length(*objects, sorted_=True, reverse=True):
    
    lengths = list(map(len, objects))
    max_length = max(lengths)
    min_length = min(lengths)
    lengths_and_objects = zip(lengths, objects)


    has_length = _('has length')
    if all(isinstance(obj, str) for obj in objects):
        predicate_max = _('and is the longest string')
        predicate_min = _('and is the shortest string')
        predicate_ave = _('and is neither the longest nor the shortest string')
    else:
        predicate_max = _('and is the longest object')
        predicate_min = _('and is the shortest object')
        predicate_ave = _('and is neither the longest nor the shortest object')

    if sorted_:
        lengths_and_objects = sorted(lengths_and_objects, reverse=reverse)

    for length, obj in lengths_and_objects:
        if length == max_length:
            predicate = predicate_max
        elif length == min_length:
            predicate = predicate_min
        else:
            predicate = predicate_ave
        print(obj, has_length, length, predicate)


A = 'I am string'
B = 'I am string too'
LIST = ["abcd", "123456789", "abcdef", "1234567"]


print('Two strings')
print()
compare_and_report_length(A, B)
print()

print('A list of strings')
print()
compare_and_report_length(*LIST)
print()
