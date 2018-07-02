size=int(input("How many elements do you want to enter: "))

array=[] #initializing array that will store user inputs

#the for loop needs to run the "size" number of times to take inputs from the user
for i in range(size):
    array.append(int(input("Enter:")))


#split function simply divides the array in half, producing two sub-arrays as a result. When size is odd, one of the sub-arr
    #ys will have more elements than the other

def split(arr):
    mid= int(len(arr)/2)
    return arr[0:mid], arr[mid: len(arr)]


#merge func uses a "two-finger" approach to forming a merged, sorted array from two sorted arrays as inputs

def merge(arr1, arr2):

    x=0
    y=0
    merge_arr=[]

    for i in range(len(arr1)+len(arr2)):
        if y>= len(arr2) or x < len(arr1) and arr1[x] > arr2[y]: #bounds testing here includes ensuring that this if statement is executed also when second sorted array has been exhausted i.e all its elemnts have been added to the merged array
            merge_arr.append(arr1[x])
            x+=1
        else:
            merge_arr.append(arr2[y])
            y+=1

    return merge_arr


#recursive func where the base case is "leaves" i.e arrays with size 1 as they are sorted by default

def merge_sort(arr):

            if len(arr)==1:
                return arr
            else:
                split_arr=split(arr)
                return merge(merge_sort(split_arr[0]),merge_sort(split_arr[1]))


print('{}'.format(merge_sort(array)))
            
            
            
            
        
