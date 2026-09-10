print(" *** Odd integer summation from 1 to n ***")
inputInteger = input("Enter an integer(n) : ")

try:
    parsed_intputInteger = int(inputInteger)

    i = 1
    total = 0
    result = ""

    if parsed_intputInteger > 0:
        while i <= parsed_intputInteger:
            total += i
            if result == "":
                result = str(i)
            else:
                result +=  f"+{i}"

            i = i + 2

        print(f"Summation => {result} = {total}")

    else:
        print(f"Summation => 0 = 0")


except ValueError:

    try:
        parsed_intputInteger = float(inputInteger)
        print(f"{inputInteger} ==> Invalid input !!!")

    except:
        print(f"{inputInteger} ==> Invalid input !!!")

print("===== End of program =====")