a=input("Enter your desired computation: ")

b=input("Enter your first number: ")

b1=int(b)

c=input("Enter your second number: ")

c1=int(c)

bc=int(b1)-int(c1)

g=int(bc)

d=1

f=1

h=1

if str(a)=="p":
    
    while(d<b1):
        b=int(b)*(b1-int(d))
        d=int(d)+1
        
    if b1==c1:
        print("The answer is %d" % b)
        
    else:

        while(f<g):
            bc=int(bc)*(g-int(f))
            f=int(f)+1
        print("The answer is %d" % (b/bc))

if str(a)=="c":

    if b1==c1:
        print("The answer is 1")
        
    else:
        
        while(d<b1):
            b=int(b)*(b1-int(d))
            d=int(d)+1
        
        while(f<g):
            bc=int(bc)*(g-int(f))
            f=int(f)+1
        
        while(h<c1):
            c=int(c)*(c1-int(h))
            h=int(h)+1
        
        print("The answer is %d" % (b/(bc*c)))
