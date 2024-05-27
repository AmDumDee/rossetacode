
import os
for directory in ['/', './']:
  open(directory + 'output.txt', 'w').close()  
  os.mkdir(directory + 'docs') 
