# a = [1,2,4,3,5,8,6]         #create list using [] brackets  
#                             #can be accessed using indices

# print(a)
# print(a[2:4])
# a.append(40)
# a[0] = 100
# print(a)

# # We  can create list for items of different Data Types


# a = ["yash" , True , 12,0,"012"]
# print(a)
# print("List Slicing\n",a[0:4])
# print("List Slicing\n",a[-5:4])      #both are same


a = [1,2,4,3,5,8,6]  

a.sort()
b = a.sort()        # Will not store sorted array in b
print(a)

a.reverse()
print("Reverse list \n",a)

a.append(30)
print("Append\n",a)

a.insert(2,12345)           # List is updated 
a.pop(4)      
a.remove(12345)                      # List Length increases
print(a)
