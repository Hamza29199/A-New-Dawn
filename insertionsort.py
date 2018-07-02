
#x stores the user input
x=input("How many numbers you wanna search through?")

array=[] #initializing array to store the numbers to be sorted



for i in range(int(x)):

    j=input("Enter a number: ")
    array.append(int(j))

dex=len(array)-1

for a in range(1, dex+1):

    x=array[a]

    b=a-1

    while b >= 0 and array[b] < x:

        array[b+1]=array[b]

        b=b-1

    array[b+1] = x

    print(array)


#so in this case the for loop goes from the second elemnt to the last; there's a purpose for this as this allows
#comparison btw a preceding element nd the next elemnt. Insertion sorts focus on inserting the right numbers in the
#right position, instead of bubbling them ahead after each pass.
