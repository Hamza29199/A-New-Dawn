"""A bit of background first-the Collatz Conjecture defines the following sequence; take any positive integer "n", if it's even, divide
it by 2, otherwise multiply it by 3 and add 1 to it. You do the same for whatever result you obtain, and keep going. The conjecture, intro
duced by Lothar Collatz in 1937, says that no matter what positive integer you start with, you will eventually reach 1. It's one of the
unsolved problems of mathematics, and while this program doesn't come up with a beautiful proof, it does print out all the terms and the
number of steps it takes for any integer to be eventually reduced to 1, as per the Collatz sequence."""

n=input("ENTER NUMBER: ") #taking user input for n here 


steps=0 #initializing integer variable steps 

while x!= 1:
    
    if int(x) %2 == 0 and x!=1: 
        
        x=int(x)/2 #if n, and any other succesive term, is even, it's halved
        steps+=1
        print(x)  #for clarity, I've decided to print out every succesive term obtained in the sequence
        
    if int(x)%2!=0 and x!=1: 
        
        x=(3*int(x))+1  #if n, and any other succesive term, is odd, it's multiplied by 3 and 1 added to result
        steps+=1
        print(x)

 #subtracting 1 because the program also counts the step at which 1 is reached, whereas I just want to display the no. of steps leading up
#to 1.

print("Conjecture ends after %d steps" % (int(c)-1)) 
