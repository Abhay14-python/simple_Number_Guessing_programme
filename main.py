from random import randint
while True:
    try:
        g = int(input("Guess a number between 1 and 100 : "))
        break
    except Exception:
        print("Invalid Input \n Please enter a valid integer")
r = randint(1,101)
tries = 1
while g != r:
    if (g>r):
        print("Try again! Guess a lower number.")
    elif (g<r):
        print("Try again! Guess a higher number : ")
    tries += 1
    g = int(input("Guess the number : "))

print(f"Correct Guess!!!. The number to guessed was {g} \n You guessed it in {tries} tries")