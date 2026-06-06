import random
n = random.randint(1, 100)
a = 1
guesses = 0
while(a!=n):
    guesses+=1
    a = int(input("guess a number : "))
    if (a> n):
        print("lower number plz...")
    elif (a< n):
        print("higher number plz...") 
    else:
        print("congratulations you have guessed the number correctly")    

print(f"YOU HAVE GUESSED THE {n} CORRECTLY IN {guesses} attempts")