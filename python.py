def find_largest_and_smallest(arr):
    if not arr:
       return None, None # return none if the array is empty
    largest=arr[0]
    smallest=arr[0]
    for num in arr:
       if num>largest:
          largest=num
       if num<smallest:
          smallest=num
    return largest, smallest
     
      #example usage:
array=[3,5,1,8,-3,7,2]
largest,smallest=find_largest_and_smallest(array)
print("largest element:",largest)
print("smallest element:",smallest)
           
           
