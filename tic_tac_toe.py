import random as rd
import math as mt
count=0
def sum(a,b,c):
    return a+b+c

def printboard(x,y):
   
    if( x[0]==1):
        zero='X'
    elif(y[0]==1):
        zero='O'
    else:
        zero='0'

    
    if( x[1]==1):
        one='X'
    elif(y[1]==1):
        one='O'
    else:
        one='1'
        
    
    if( x[2]==1):
        two='X'
    elif(y[2]==1):
        two='O'
    else:
        two='2'

    
    if( x[3]==1):
        three='X'
    elif(y[3]==1):
        three ='O'
    else:
        three='3'

    
    if( x[4]==1):
        four='X'
    elif(y[4]==1):
        four='O'
    else:
        four='4'


    if( x[5]==1):
        five='X'
    elif(y[5]==1):
        five='O'
    else:
        five='5'


    if( x[6]==1):
        six='X'
    elif(y[6]==1):
        six='O'
    else:
        six='6'


    if( x[7]==1):
        seven='X'
    elif(y[7]==1):
        seven='O'
    else:
        seven='7'


    if( x[8]==1):
        eight='X'
    elif(y[8]==1):
        eight='O'
    else:
        eight='8'     
        
        
    
 
  
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|--")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight} ")

def checkwin(x,y,t):
    
    b=1
    c=1
    wins=[[0,1,2], [3,4,5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in wins:
       # a=a+1
        
        if(sum(x[i[0]], x[i[1]], x[i[2]]) == 3):
            print("X Won the match")
            printboard(x,y)
            b=0
            
            return 1
            
        if(sum(y[i[0]], y[i[1]], y[i[2]]) == 3):
            print("O Won the match")
            printboard(x,y)
            c=0
            return 0
        
    if((t==9 and sum(x[i[0]], x[i[1]], x[i[2]]) != 3 ) and  (t==9 and sum(y[i[0]], y[i[1]], y[i[2]]) != 3)):
        return 2
        
       
        
    return -1
    


if __name__ == "__main__":
   
    x=[0,0,0,0,0,0,0,0,0]
    y=[0,0,0,0,0,0,0,0,0]

    print("\"Welcome to Tic Tac Toe game\"")
    l=[0,1]
    turn=rd.choice(l)
    t=0
   
    while(True):
        printboard(x,y)
      #turn=rd.choice(l)
        if(turn == 0):
            t=t+1

            print("0's chance")
            
            value=int(input("Enter the value: "))
            y[value]=1
            #checkwin(value)
            turn=turn+1
        else:
            t=t+1
            
            print("X chance")
            value=int(input("Enter the value: "))
            x[value]=1
            turn=turn-1
            
                      
        win=checkwin(x,y,t)
        
        if(win==2):
            print("Game Draw !!")
            print("Press 1 to play again or 0 to exit")
            e=int(input())
            if(e==0):
                print("Thank you for playing!!")
                break
            else:
                x=[0,0,0,0,0,0,0,0,0]
                y=[0,0,0,0,0,0,0,0,0]
                turn=rd.choice(l)
                continue
            
    
        if(win!=-1):
            print("Game Over")
            print("Press 1 to play again or 0 to exit")
            e=int(input())
            if(e==0):
                print("Thank you for playing!!")
                break
            else:
                x=[0,0,0,0,0,0,0,0,0]
                y=[0,0,0,0,0,0,0,0,0]
                turn=rd.choice(l)
                continue
        
