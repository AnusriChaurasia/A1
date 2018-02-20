import random as r
compscore=0
myscore=0
conditions={'Rock':'Scissors','Paper':'Rock','Scissors':'Paper'}
L=['Rock','Paper','Scissors']
while (True):
    mychoicenum=int(input("Enter \n 1 for Rock \n 2 for Paper \n 3 for Scissors: "))
    mychoice=L[mychoicenum-1]
    compchoice=r.choice(L)
    if compchoice==mychoice:
        print("Tie.")
    elif(conditions[compchoice]==mychoice):
        print("Computer wins with",compchoice)
        compscore+=1
    elif(conditions[mychoice]==compchoice):
        print("You win with",mychoice)
        myscore+=1
    if(compscore==5):
        print("Computer wins!")
        break
    if(myscore==5):
        print("You win!")
        break
    print("End of Round. Scores are:")
    print("Computer:",compscore)
    print("You:",myscore)
    print('****************************************************')
print("Press <Enter> to continue")
