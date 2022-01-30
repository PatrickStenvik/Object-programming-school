
x = int(input("Anna tehtyjen tehtävien määrä: "))
if (x < 60):
    print("arvosanasi on: 0")
elif (x < 60, x > 72):
    print("arvosanasi on: 1")
elif (x < 72, x > 84):
    print("arvosanasi on: 2")
elif (x < 84, x > 96):
    print("arvosanasi on: 3")
elif (x < 96, x > 108):
    print("arvosanasi on: 4")
else:
    print("arvosanasi on: 5")