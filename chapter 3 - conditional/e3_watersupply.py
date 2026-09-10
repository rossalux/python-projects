print(" *** Water Supply Calculator ***")
totalUsage = int(input("Total usage : "))
totalAmount = 0

if totalUsage > 5000:
    totalUsage = totalUsage - 5000
    totalUsage = totalUsage * 21
    totalAmount += totalUsage

    totalUsage = 5000

if totalUsage > 1000:
    totalUsage = totalUsage - 1000
    totalUsage = totalUsage * 20
    totalAmount += totalUsage

    totalUsage = 1000

if totalUsage > 500:
    totalUsage = totalUsage - 500
    totalUsage = totalUsage * 18
    totalAmount += totalUsage

    totalUsage = 500

if totalUsage > 100:
    totalUsage = totalUsage - 100
    totalUsage = totalUsage * 15
    totalAmount += totalUsage

    totalUsage = 100

if totalUsage > 50:
    totalUsage = totalUsage - 50
    totalUsage = totalUsage * 12
    totalAmount += totalUsage

    totalUsage = 50

if totalUsage > 10:
    totalUsage = totalUsage - 10
    totalUsage = totalUsage * 10
    totalAmount += totalUsage

    totalUsage = 10

if totalUsage > 0:
    totalUsage = totalUsage * 5
    totalAmount += totalUsage

totalAmount = float(totalAmount)

print(f"{totalAmount:,.2f} baht")
