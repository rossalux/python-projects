print(" *** Min Max Avg ***")
one, two, three = input("Enter 3 numbers : ").split()

a = float(one)
b = float(two)
c = float(three)

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

average = (a+b+c)/3

print(f"{'min, mid, max ==>'}", f"{a}, {b}, {c}")
print(f"Average ==>", f"{average:.2f}")