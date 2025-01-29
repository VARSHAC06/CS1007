array=[3,5,1,8,-3,7,2]

max=array[0]
min=array[0]
for num in array:
    if num>max:
        max=num
    if num<min:
        min=num
print(f"largest element: {max}")
print(f"smallest element: {min}")
           
