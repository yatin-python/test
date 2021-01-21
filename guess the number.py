rg = 18
g=9
while(True):
    print("you have ",g ,"Guess left")
    print("enter number :-")
    num = int(input())
    if g==1:
        print("Game Over Bye Bye the right number is 18")
        break

    if g<=9:
        if num>rg:
            print("your number is gretor try again")
            g=g-1
        elif num<rg:
            print("your number is lesser try again")
            g=g-1
        elif num==rg:
            print("you enter a right number you win the match ")
            break
