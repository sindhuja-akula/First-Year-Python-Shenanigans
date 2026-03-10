import sys
import numpy as np
try:
    n=int(input("enter size of tic_tac_toe_box that you want to play with"))
    for i in range(n+1):
        if(i<n):
            print("----"*(n),end="")
            print("-")
            print("|   "*(n+1))
        elif(i==n):
            print("----"*(n),end="")
            print("-")  
    box=np.full((n,n),' ')
except e as valueError:
    print(e)

def board(row,column,i):   
                    
    if i%2==0:
        box[row][column]="X"
    else:
        box[row][column]="O"
    for i in range(n):
        r=box[i]
        if(i<n):
            print("----"*(n),end="")
            print("-")
            for j in range(n):
                print(f"| {box[i][j]} ",end="")
            print("|")
    print("----"*(n),end="")
    print("-")  
    winner(box)
def winner(box):
    dic={"X":"Player 1","O":"Player 2"}
    for i in range(n):
        count1=0
        count2=0
        r=box[i]
        if(r[i] in ["X","O"] ):
            left_dia=[box[j][j] for j in range(n) if r[i]==box[j][j]]
            right_dia=[box[j][n-j-1] for j in range(n) if (r[n-i-1]==box[j][n-j-1] and r[n-i-1]!=' ')]
    
    
            if(list(r).count(r[i])==n):           
                print(f"The winner is{dic[r[i]]} through row")
                sys.exit()
            elif (list(box[:,i:i+1]).count(r[i])==n):
                print(f"The winner is {dic[r[i]] }through column")
                sys.exit()
                
           
            if(len(left_dia)==n):
                print(f"The winner is{dic[r[i]]} thrgh left dia")
                sys.exit() 
            elif(len(right_dia)==n):
                print(f"The winner is{dic[r[i]]} thrgh right dia")
                sys.exit()             
i=0
while i<(n*n):
    row,column=[int (i) for i in input("please enter row and column in row,column form").split(",")]
    print(f"you have choosen {row} {column} position")
    if (box[row][column])!=' ':
        print(i)
        print("this postion is choosen already\n")
        i=i-1
    elif (str(row).isdigit()) and (str(column).isdigit()) :
        row=int(row)
        column=int(column)
       
        board(row,column,i)
    else:
        print("invalid input")
        i=i-1
    i+=1
print("no one wins, it's a draw")
