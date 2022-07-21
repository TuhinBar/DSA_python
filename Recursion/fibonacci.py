# Great starter for recursion

def getFib(n):
    if n==1:
        return 1
    return n + getFib(n-1)

# driver code
print(getFib(5))