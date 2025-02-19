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
    
ejemplo="(())((()))()"

print(revisar(ejemplo))