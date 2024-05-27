import base64 # for b64encode()
from urllib.request import urlopen

print(base64.b64encode(urlopen('http://rosettacode.org/favicon.ico').read()))
