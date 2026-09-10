print(" *** Digit count and Summation ***")

inputInteger = int(input("Enter an integer : "))
print(f"Entered number = {inputInteger:,}")

totalDigit = str(inputInteger)
print(f"Total digits are: {len(totalDigit)}")

i = 0

while i <= inputInteger:
    