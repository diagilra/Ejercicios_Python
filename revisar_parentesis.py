from collections import deque

def revisar(s):
    stack=[]
    for elem in s:
        if elem == "(":
            stack.append(elem) 
        elif elem == ")":
            if len(stack)>0:
                stack.pop(-1)
            else:
                return False
    if len(stack)!=0:
        return False
    else:
        return True

# También puedo crear la función con un deque para que sea más rápido
def revisar_parentesis(s):
    deq=deque()
    for elem in s:
        if elem == "(":
            deq.append(elem) 
        elif elem == ")":
            if len(deq)>0:
                deq.pop()
            else:
                return False
    if len(deq)!=0:
        return False
    else:
        return True    


ejemplo="(())((()))()"



print(revisar(ejemplo))

