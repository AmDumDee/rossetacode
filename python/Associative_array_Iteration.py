myDict = { "hello": 13,
       "world": 31,
       "!"    : 71 }

for key, value in myDict.items():
    print ("key = %s, value = %s" % (key, value))

for key in myDict:
    print ("key = %s" % key)

for key in myDict.keys():
    print ("key = %s" % key)

for value in myDict.values():
    print ("value = %s" % value)
