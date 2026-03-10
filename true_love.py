from functools import reduce
l=[i for i in input("enter people name's\n").split(",")]
l=[i.lower() for i in l]
total=reduce(lambda x,y:x+y,l)
true=[total.count(i)for i in total if i in "true"]
love=[total.count(i)for i in total if i in "love"]
if(len(true)!=0):
    true=reduce(lambda x,y:x+y,true)
else:
    true=0
if(len(love)!=0):
    love=reduce(lambda x,y:x+y,love)
else:
    love=0
l=str(l)
print(f"{l}'s love is {true}{love} % true love")
 
