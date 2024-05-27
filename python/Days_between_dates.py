
import sys



def days( y,m,d ):
  
  m = (m + 9) % 12 
  y = y - m/10

  
  result = 365*y + y/4 - y/100 + y/400 + (m*306 + 5)/10 + ( d - 1 )
  return result

def diff(one,two):
  [y1,m1,d1] = one.split('-')
  [y2,m2,d2] = two.split('-')
  
  year2 = days( int(y2),int(m2),int(d2))
  year1 = days( int(y1), int(m1), int(d1) )
  return year2 - year1

if __name__ == "__main__":
  one = sys.argv[1]
  two = sys.argv[2]
  print(diff(one,two))
