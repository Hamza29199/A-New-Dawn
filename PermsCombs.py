"""A program which computes permutations and combinations of values entered by user"""

#following function takes in an int parameter
# and computes its factorial recursively

def factorial(num):

	if num > 1:

		return num * factorial(num-1)


	return 1 #the terminating condition for our recursive func



#defining functions for determining perms and combs below

def permutation(n, r):

	return (factorial(n)/factorial(n-r))


def combination(n, r):

	return (factorial(n)/(factorial(n-r) * factorial(r)))


#taking user inputs for the computation, and values of n and r

choice = str(input("Which computation would you like to perform?(Enter ""p"" or ""c"" for perm and comb respectively)"))

n= int(input("Enter the number of objects in your set(n): "))



if(choice == "p"):
    r= int(input("Enter the number of times you want to permute your objects(r): "))
    print("Your result is %d.", permutation(n, r))


elif(choice == "c"):
    r= int(input("Enter the number of times you want to combine your objects(r): "))
    print("Your result is %d.", combination(n, r))
