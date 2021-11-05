# ADIA Problem Sheet 4 - q3
# simple hash
import string
print(string.ascii_uppercase)
def dict (mod=26,n=0):
    v = 0
    dictionary = {}
    for k in string.ascii_uppercase:
        dictionary[k] = v%mod+n
        v+=1
    print(dictionary)
    return
            
# manipulating this cos im lazy

dict(7,1)
dict(11,0)



"""
k = "E,L,E,C,T,R,O,N,I,C,I,D,E,N,T,I,T,Y"
kk = k.split(",")
print(kk, "\n")
dict(kk)

# actual code
dicto = {}
value = 0
for key in string.ascii_uppercase:
    dicto[key] = value
    value+=1
    
print("dict\n", dicto, "\n")

# edit for h1
h1 = {}
value = 0
for key in string.ascii_uppercase:
    h1[key] = (value%7)+1
    value+=1

print("h1\n", h1, "\n")

# edit for h2
h2 = {}
value = 0
for key in string.ascii_uppercase:
    h2[key] = value%11
    value+=1

print("h2\n", h2, "\n")
"""
