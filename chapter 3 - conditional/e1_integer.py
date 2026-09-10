print(" *** Integer Property ***")
wholeNumber = input("Enter a whole number : ")
try:
    wholeNumber = int(wholeNumber)

    if wholeNumber > 0:
        label = "positive integer"
    elif wholeNumber < 0:
        label = "negative integer"
    else:
        label = "zero integer"

    print(f"{'type =>':>15}", f"{label}")

    if wholeNumber < 0:
        magnitude = -wholeNumber
    else:
        magnitude = wholeNumber

    print(f"{'Magnitude =>':>15}", f"{magnitude}")

    if wholeNumber %2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    print(f"{'Parity =>':>15}", f"{parity}")
    
    print("===== End of program =====")
    
except:
    wholeNumber = float(wholeNumber)

    if wholeNumber == float(wholeNumber):
        print()
