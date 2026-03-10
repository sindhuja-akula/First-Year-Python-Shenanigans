def number_guess(chances,r):
    numb_to_guessed=r
    n=int(input("make a guess\n"))
    for i in range(1,chances+1):
        if(numb_to_guessed-5<n<numb_to_guessed or numb_to_guessed<n<numb_to_guessed+5):
            print("\nyour close")
        elif(n<numb_to_guessed-5):
            print("\nyour low")
        elif(n>numb_to_guessed+5):
            print("\nyour high")
        elif n==numb_to_guessed:
            print("\nyour guess is correct")
            sys.exit()
        
        n=int(input("make a guess\n"))
        print(f"you have {chances-i} attempts\n")
        
import random
import sys
print("\n"
" ***** **  **  ******   ******   ******    ******** **       ******     **    ** **  **  **    **  **       ******  *\n"
"****** **  ** ******** ******** ********   ******** **      ********    **    ** **  ** ****  **** **      ******** ** ****\n" 
"**     **  ** **    ** **       **            **    ** **   **    **    ***   ** **  ** **  **  ** **      **    ** ********\n"
"**     **  ** ******** ******** ********      **    ******* ********    ****  ** **  ** **  **  ** ** ***  ******** **    **\n"
"**  ** **  ** ******** ******** ********      **    **   ** ********    ** ** ** **  ** **  **  ** ******* ******** **\n"
"**  ** **  ** **             **       **      **    **   ** **          **  **** **  ** **  **  ** **   ** **       **\n"
"****** * ** * ******** ******** ********      **    **   ** ********    **   *** * ** * **  **  ** ******* ******** **\n"
" ****   ****   ******   ******   *****        **    **   **  ******     **    **  ****  **  **  ** ** ***   ******  **\n")
l=[range(0,50),range(50,100),range(100,150),range(150,200),range(200,250),range(250,300),range(300,350),range(350,400),range(400,450),range(450,500),range(500,550),range(550,600),range(600,650),range(650,700),range(700,750),range(750,800),range(800,850),range(850,900),range(900,950),range(950,1001)]
value=random.choice(l)
print(f"let me  think of a number b/w {value},both inclusive\n")
r=random.choice(value)
level=input("choose level of difficulty type \neasy\thard\n")
while level!="easy" and level !="hard":
    level=input("choose level of difficulty type \neasy\thard\n")    
attempts=[10,5]
if level=="easy" :
    print(f"you have {attempts[0]} attempts remaining to guess the number\n") 
    chances=attempts[0]
else: 
    print(f"you have {attempts[1]} attempts remaining to guess the number\n")
    chances=attempts[1]
number_guess(chances,r)



