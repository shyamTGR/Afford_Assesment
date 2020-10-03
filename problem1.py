class A:
    def check(self, b, w):
        if not w or not any(b): return False
        
        e, f = len(b),len(b[0])
        def df(c, d, i = 0):
            
            if i == len(w) - 1: return b[c][d] == w[i]
            if b[c][d] != w[i]: return False
            
            value = b[c][d]
            
            b[c][d] = ' '
            
            for r, c1 in (c+1, d), (c-1, d), (c, d+1), (c, d-1):
                if 0 <= r < e and 0 <= c1 < f and df(r, c1, i + 1):
                    return True
            b[c][d] = value
            return False

        return any(df(c, d) for c in range(e) for d in range(f))
        
b=[
['A','B','C','E'],
['S','F','C','S'],
['A','D','E','E']
]
w="ABCCED"
#Works for any input given, just using example given in assesment 
s=A()
print(s.check(b,w))

