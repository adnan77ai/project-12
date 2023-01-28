import sys
sys.setrecursionlimit(2000)
i = 0
def hi():
  global i
  i += 1
  print ('Hello', i)
  hi()
 
hi()

