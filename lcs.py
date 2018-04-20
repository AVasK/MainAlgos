# Longest Common Subsequence:
# code written late in the night, so it looks kinda bizarre))

# Input: 
## 2 strings:
## -> X - sequence 1
## -> Y - sequence 2
# Output:
## -> length of the longest subsequence

def LCS_matrices(X, Y, debug = False):
    m = len(X)
    n = len(Y)
    b = [[' ' for _ in range(0, n+1)] for _ in range(0, m+1)]
    c = [[0 for _ in range(0, n+1)] for _ in range(0, m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = '\\'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "^"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "<"
                
    if debug:
        for line in c:
            print(line)
    
        for line in b:
            print(line)
    
    return c, b


def LCS_len(c):
    return c[-1][-1]

def LCS_construct(X, Y, b):
    m = len(X)
    n = len(Y)
    
    ans = ''
    
    i = m
    j = n
    
    while i != 0 and j != 0:
        if b[i][j] == '\\':
            ans += X[i-1]
            i -= 1
            j -= 1
        elif b[i][j] == '^':
            i -= 1
        else:
            j -= 1
            
    return ans[::-1]

def LCS_standalone(X, Y):
    c, b = LCS_matrices(X, Y)
    return LCS_construct(X, Y, b)


X = input("sequence 1: ")
Y = input("sequence 2: ")

c, b = LCS_matrices(X, Y)
print("Longest common subsequence length: ", LCS_len(c))
print("Longest common subsequence: ", LCS_construct('ABBCE', 'ACE', b))


