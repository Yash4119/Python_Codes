# my_dict = {
#     "fast" : "in a  quick manner",
#     "harry" : "a coder",
#     "marks" : 35,
#     "new_dict" : {"roll" : 24,"id" : 25,"yash" : "a noobie"},
# }
# print(my_dict["fast"])
# print(my_dict["harry"])
# print(my_dict["marks"])
# print(my_dict["new_dict"]["roll"])
# print(my_dict["new_dict"]["yash"])
# print(my_dict.keys())
# # typecasting
# print(list(my_dict.keys()))        
# print(my_dict.values()) 
# print(my_dict.items())
# update = {
#     "lovish":"harry's partner",
# }
# my_dict.update(update)
# print(my_dict)

# # diff between .get and [ ] function of dictonary
# print(my_dict.get("harry2"))        #returns none if key is not present in dictonary
# print(my_dict["harry2"])        #returns error key is not present in dictonary


a = {1,2,3,5,1,2}
# sets is collection  of non repititive items
print(type(a))

b = {}      #empty dictonary
print(type(b))

c = set()
print(type(c))
c.add(1)
c.add(34)
print(c)
# cannot add a list in a set
# but we can add a tuple to a set
# becoze set is hashable so we can add only hashable data types
# set is immutable and also cannot contain duplicae values
print(len(c))
c.remove(34)        #gives error if element is not present in the set
c.add(2)
c.add(9)
c.add(5)
c.pop()
print(c)




