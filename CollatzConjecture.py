

x=input("ENTER NUMBER: ")
c=0
while x!= 1:
    if int(x) %2 == 0 and x!=1:
        x=int(x)/2
        c=c+1
        print(x)
    if int(x)%2!=0 and x!=1:
        x=(3*int(x))+1
        c=c+1
        print(x)

print("Conjecture ends after %d steps" % (int(c)-1))
