def balanced(testVariable, startIndex = 0, currentIndex = 0) :
      # Base case1 and 2
  if startIndex == len(testVariable) : 
    return currentIndex == 0

  # Base case3
  if currentIndex < 0 : # A closing bracket did not find its corresponding opening bracket
    return False

  # Recursive case1
  if testVariable[startIndex] == "(" : 
    return  balanced(testVariable, startIndex + 1, currentIndex + 1)

  # Recursive case2
  elif testVariable[startIndex] == ")" : 
    return  balanced(testVariable, startIndex + 1, currentIndex - 1)

# Driver Code
testVariable = ["(", "(", ")", ")", "(", ")"]
print(balanced(testVariable))