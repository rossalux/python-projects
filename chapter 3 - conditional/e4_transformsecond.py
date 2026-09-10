print(" *** Transform second ***")
inputSecond = input("Enter seconds : ")

try:
    parsed_InputSecond = int(inputSecond)
    totalSecond = parsed_InputSecond
    

    if parsed_InputSecond > 0:
        # Total per quantities
        week = 0
        day = 0
        hour = 0
        minute = 0
        second = 0

        # Quantities format
        weekFormat = ""
        dayFormat = ""
        hourFormat = ""
        minuteFormat = ""
        secondFormat = ""

        if parsed_InputSecond >= 604800:
            week = parsed_InputSecond // 604800
            parsed_InputSecond = parsed_InputSecond % 604800

            if week > 1:
                weekFormat = "weeks"
            elif week == 1:
                weekFormat = "week"
            else:
                weekFormat = ""

        if parsed_InputSecond >= 86400:
            day = parsed_InputSecond // 86400
            parsed_InputSecond = parsed_InputSecond % 86400

            if day > 1:
                dayFormat = "days"
            elif day == 1:
                dayFormat = "day"
            else:
                dayFormat = ""

        if parsed_InputSecond >= 3600:
            hour = parsed_InputSecond // 3600
            parsed_InputSecond = parsed_InputSecond % 3600

            if hour > 1:
                hourFormat = "hours"
            elif hour == 1:
                hourFormat = "hour"
            else:
                hourFormat = ""

        if parsed_InputSecond >= 60:
            minute = parsed_InputSecond // 60
            parsed_InputSecond = parsed_InputSecond % 60

            if minute > 1:
                minuteFormat = "minutes"
            elif minute == 1:
                minuteFormat = "minute"
            else:
                minuteFormat = ""

        if parsed_InputSecond > 0:
            second = parsed_InputSecond

            if second > 1:
                secondFormat = "seconds"
            elif second == 1:
                secondFormat = "second"
            else:
                secondFormat = ""

        print(f"{totalSecond} seconds ==>", end=" ")

        if week > 0:
            print(f"{week} {weekFormat}", end=" ")
        if day > 0:
            print(f"{day} {dayFormat}", end=" ")
        if hour > 0:
            print(f"{hour} {hourFormat}", end=" ")
        if minute > 0:
            print(f"{minute} {minuteFormat}", end=" ")
        if second > 0:
            print(f"{second} {secondFormat}", end=" ")

        print()

    elif parsed_InputSecond < 0:
        print(f"This number ({inputSecond}) is not VALID !!!") 
    else:
        print(f"{inputSecond} ==> 0 second")

except ValueError:

    try:
        parsed_InputSecond = float(inputSecond)

        print(f"! ! ! please enter a whole number ==> {parsed_InputSecond}")

    except ValueError:
        print(f"This number ({inputSecond}) is not VALID !!!")

print("===== End of program =====")