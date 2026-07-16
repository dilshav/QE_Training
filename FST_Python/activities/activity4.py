# Rules
# Two players
# Choose: Rock, paper, scissor
# Win conditions
# Rock beats scissors
# scissors beats paper
# paper beats rock



while True:
    p1=input("Player1 : Enter your move: ").lower()
    p2=input("Player2 : Enter your move: ").lower()

    if p1==p2:
        print("Iy's a tie")
    elif p1=="rock":
        if p2=="paper":
            print("p2 wins")
        else:
            print("p1 wins ")
    elif p1=="paper":
        if p2=="scissors":
            print("p2 wins")
        else:
            print("p1 wins")
    elif p1=="scissors":
        if p2=="rock":
            print("p2 wins")
        else:
            print("p1 wins")
    else:
        print("Invalid")

    gm=input("Do you wanna continue: (yes/no): ").lower()
    if gm=="no":
        break
    
    


