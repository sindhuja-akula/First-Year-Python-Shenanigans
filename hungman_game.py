def man(count):
    print(guess)
    print("_"*8)
    if(count==0):
        for i in range(5):
            print(" "*5,"|")
    else:
        for i in range(count):
            if(i==2 or i==5):
                print(d[i],end="")
            elif(i==3 or i==6):
                print(d[i],"|")
            else:
                print(d[i]," |")
        for k in range(5-i+1):
            if(k==0 and i==2 or k==0 and i==5):
                print("  |")
            else:        
                print(" "*5,"|")    
    print("*"*7,end="")        
import sys
import random
l = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "mango", "orange", "watermelon"]
s = random.choice(l)
print("clue:it is a fruit")
d=["   o","   |","  \|","/","   |","  /|","\\"]
count=0
win=0
guess=['_']*len(s)
for i in range(len(s)+7):
    ch=input("\nenter your guess\n")
    ch=ch.lower()
    if ch in guess:
        print("you have guessed this word already,try guessing another letter")
        i-=1
    elif ch not in s:
        count+=1
        man(count)
        if(count==7):
                print("you loss\n")
                sys.exit()
        print(f"you left with {7-count} chances")
    else:
        if s.count(ch)==1:
            i=s.index(ch)
            guess[i]=ch
            man(count)
            if(list(s)==guess):
                print("you won")
                sys.exit()          
        else:
            i=0 
            j=0
            for k in range(s.count(ch)):
                i=s[i:len(s)].index(ch)
                guess[i+j]=ch
                i=i+1
                j=i
                print(i)
            man(count)
            if(s==guess):
                print("you won")
                sys.exit() 
