# Great starter for recursion

def getFib(n):
    if n==1:
        return 1
    return n + getFib(n-1)

# driver code

print(getFib(5))

# Alternate solution
def getFib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return getFib(n-1) + getFib(n-2)