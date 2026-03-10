size=input("enter the size \n 1)small\t2)medium\t3)large\n")
flavr=input("flavour\n1)cheese\t2)pepperone\t3)valcano\n")
cheese=input("do you want extra cheese,enter yes or no")
d={'small':100,'medium':200,'large':300}
flav={'cheese':20,'pepperone':30,'valcano':40}
extra={'yes':20,'no':0}
print("the total cost is",d[size]+flav[flavr]+extra[cheese])

