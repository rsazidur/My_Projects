low = 1
high = 1000

print(f"Please think a number a number between {low} to {high}.")
input("Please ENTER to start.")

guesses = 1
while True:
    print(f"\t\t\tGuessing in the range {low} to {high}")
    guess = low + (high - low) // 2
    high_low = input(f"My guess is {guess}.\nShould i guess higher or lower? "
                     "Enter h or l or c if my guess is correct: ").casefold()

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print(f"I got it in {guesses} guesses!")
    else:
        print("Enter 'h', 'l' or 'c' ")

    guesses = guesses + 1