import time
'''
This recurs n times. each run is 3^N Total is O(n * 3^n)
'''

def letterCombinationsSlow(digits):
  store = {
   '2': ['a','b','c'],
   '3': ['d','e','f'],
   '4': ['g','h','i'],
   '5': ['j','k','l'],
   '6': ['m','n','o'],
   '7': ['p','q','r', 's'],
   '8': ['t','u','v'],
   '9': ['w','x','y','z'],
  }
    
  if len(digits) == 1:
    return store[digits]
  else:
    before = letterCombinationsSlow(digits[0: len(digits)-1]) #n
    currLetter = store[digits[len(digits)-1]]
    return [before[j] + currLetter[i] for i in range(len(currLetter)) for j in range(len(before))] #3^N

        #total n^4

def letterCombinationsFast(digits):
  comboMap = {
   '2': ['a','b','c'],
   '3': ['d','e','f'],
   '4': ['g','h','i'],
   '5': ['j','k','l'],
   '6': ['m','n','o'],
   '7': ['p','q','r', 's'],
   '8': ['t','u','v'],
   '9': ['w','x','y','z'],
  }
  
  result = []
  
  def recur(acc, digits):
    if len(digits) == 1:
      for child in comboMap[digits]:
          result.append(acc + child)
    else:
      size = len(digits)
      for child in comboMap[digits[0]]:
        recur(acc+child, digits[1:size])
              
  if len(digits) != 0:
    recur('', digits) 
  
  return result

def sum(n):
  start = time.time()

  for i in range(n):
    letterCombinationsSlow('5474')

  end = time.time()

  return end-start

#print(letterCombinationsS('54754876576576576576'))

print(sum(1000000))