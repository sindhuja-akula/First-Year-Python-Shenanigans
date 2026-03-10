import random
def precedence(person,computer):
    if((person=="rock" and computer=="sicssors")or (computer=="rock" and person=="sicssors") ):
        return "rock"
    elif((person=="rock" and computer=="paper" )or (computer=="rock" and person=="paper")):
        return "paper"
    elif((person=="paper" and computer=="sicssors") or( computer=="paper" and person=="sicssors")):
        return "sicssors"
  
person=input("enter your choice \n1)rock\t2)paper\t3)sicssors\n")
print("person choice is",person)
l=["rock","paper","sicssors"]
while(True):
    if(person not in l):      
        person=input("invalid choice\n please enter from below options \n1)rock\t2)paper\t3)sicssors\n")
    else:
        break
computer=random.choice(l) 
print("\ncomputer choice is",computer,"\n")
win=precedence(person,computer)
if win==person:
    print("person wins")
elif win==computer:
    print("computer wins")
else:
    print("no one wins as both are same")




