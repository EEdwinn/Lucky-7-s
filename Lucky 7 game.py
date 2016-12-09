###Lucky 7

###
#Lucky Sevens
###

#Start wiht $10,every game costs $1 to play
#roll two dice
#if the result is seven, win $5(+$4 overall after the $1 cost)
#The game contunuously plays untiol you run out of money.
#At the end,it tells you how many rounds were played.


import random
import sys
money=10
turn=0
while money!=0:
    dice=random.randint(1,6)
    dice2=random.randint(1,6)
    total=dice+dice2
  
    print "Your number is " +str(dice+dice2)

    if total ==7:
        print "You Win"
        money += 4
        print "Your money is:%d" % money
        turn +=1
    else:
        print "You lose the round"
        money -=1
        print "Your money is:%d" % money
        turn +=1
        print "Your total rounds were: %d"% turn
        
        
       

    


        
