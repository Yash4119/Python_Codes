a = "yash's House or "  #Using ' in the string
b = 'Yash"s House'
print(a,"\n",b)
c = a+b
print(c[0:20:2])        #we are not allowed to change any element of a string
                        # c[0:20:2] == c[start : end : step]
                            # while printing the element before the end is printed 