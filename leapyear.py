print("\t\tfind a leap year using if else")
year = int(input("Enter a year: ",))

# Check if it's a leap year
if year % 4 == 0 :
    print(f"{year} is a leap year.", 'red')
else:
    print(f"{year} is not a leap year.")