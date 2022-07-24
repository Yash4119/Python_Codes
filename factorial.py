def fact_recursive(n):
    if(n==1 or n==0):
        return 1

    return n*fact_recursive(n-1)

f = fact_recursive(0)
print(f)