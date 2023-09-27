def fact(s):
  if s == 0:
    return 1
  else:
    return s * fact(s - 1)


print("\t\t factorial using recursive function")
s = int(input("Enter a number: "))

if s < 0:
  print("Factorial is not defined for negative numbers.")
else:
  result = fact(s)
  print(f"The factorial of {s} is {result}")