x=input("How many numbers you wanna search through?")

array=[]



for i in range(int(x)):

    j=input("Enter a number: ")
    array.append(int(j))

#initializing bubble sort algorithm 

dex= len(array)-1

a=0

while a <=dex:
    
    
    for b in range(1,dex):
    

        if array[b] > array[b+1]:
            
        

            temp=array[b]
            array[b]=array[b+1]
            array[b+1]= temp

    a=+1

#so the above while loop makes a pass through the series of numbers; the nested for loop compares each element to ensure
#that the largest elements in each pass get bubbled all the way up e.g in the first pass, the largest (or smallest) element
#gets bubbled to the end
print(array)
