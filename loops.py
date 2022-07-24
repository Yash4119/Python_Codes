
# a = 4
# fact = 1
# for i in range(1,a+1):
#     fact = fact*i

# print(f"Factorial of {a} is {fact}")


# patterns
# * 
# * *
# * * *
# * * * *
# * * * * *

# a = 5
# for i in range(a):
#     print("* "*(i+1))


# pattern two

a = 3
for i in range(a):
    print(" "*(a-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(a-i-1))
