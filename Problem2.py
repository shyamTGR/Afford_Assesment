def check(string):
    st = []
    brackets = {"(": ")", 
                "[": "]",  
                "{": "}"}
    
    start = list(["(", "[", "{"])
    
    for i in string:
        if i in start: st.append(i)
        elif st and i == brackets[st[-1]]: st.pop()
        
        else: return False
    return st == []
    
string=input()
print(check(string))
