s = input()
count = 0
while count < 2**64:
    delete_stack = []
    for i in range(len(s)-2):
        if s[i] == s[i+1] and s[i+1]!=s[i+2]:
            delete_stack.append(i+1)
            delete_stack.append(i+2)
        if s[i] != s[i+1] and s[i+1]==s[i+2]:
            delete_stack.append(i+1)
            delete_stack.append(i)
    delete_stack = list(set(delete_stack))
    ss = list(s)
    s = ""
    for i in range(len(ss)):
        if i not in delete_stack:
            s += ss[i]
    if len(s) == 0:
        print("EMPTY")
        break
    if len(delete_stack) == 0:
        print(s)
        break
        
    
    
