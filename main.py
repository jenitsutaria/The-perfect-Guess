import random
a = random.randint(1,100)
n = -1
guesses = 1

while(n != a):
    n = int(input("Enter your guess: "))
    if(n>a):
        print("Lower number please")
        guesses += 1
    elif(n<a):
        print("Higher number please")
        guesses += 1

print(f"You have guessed the number which was {a} in {guesses} attempt")