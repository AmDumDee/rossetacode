hash = dict()  
hash = dict(red="FF0000", green="00FF00", blue="0000FF")
hash = { 'key1':1, 'key2':2, }
value = hash[key]



d = {}
d['spam'] = 1
d['eggs'] = 2

d1 = {'spam': 1, 'eggs': 2}
d2 = dict(spam=1, eggs=2)

d1 = dict([('spam', 1), ('eggs', 2)])
d2 = dict(zip(['spam', 'eggs'], [1, 2]))

for key in d:
  print (key, d[key])

for key, value in d.iteritems():
  print (key, value)



myDict = { '1': 'a string', 1: 'an integer', 1.0: 'a floating point number', (1,): 'a tuple' }
