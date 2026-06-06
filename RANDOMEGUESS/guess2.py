import random
guess = 0 
n = random.randint(1, 100)
while True:

    a =int(input("guess a number : "))
    guess+=1
    if a>n:
        print("lower number plz...")
    elif a<n:
        print("higher num plz...")
    else :
        print(f"congratulations u found it in {guess} attempts")
        break    
