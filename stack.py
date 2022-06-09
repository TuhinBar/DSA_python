from sys import maxsize

def isEmpty(self):
    return True if self.value is None else False

def stPop(stack):
    if(stack.isEmpty()):
        return str(-maxsize-1)
    return stack.pop()
    # if(pop<=0):
    #     return 0;
    # else:
    #     for i in range(0,pop):
    #         stack.pop()
stack=[22,21,21,11,2,3,43,2,55]


# print('Enter the elements to fill the stack:')
# for i in range(0,numOfElement):
#     i=int(input())
#     stack.append(i)

print('The stack is',stack)

# pop=int(input('Enter the number of elements you ant to pop'))
print(stPop(stack)+ "poped from stack")
# if(pop<=0):
#     print('no items to be popped')
# else:
#     for i in range(0,pop):
#         stack.pop()

