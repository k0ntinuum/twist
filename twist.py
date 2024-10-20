from numpy.random import permutation
from numpy.random import randint
def rotate(l, n):
    return l[-n:] + l[:-n]

step = 4
base = 2


def dec_from_bin(x):
    y = []
    for s in range(0, len(x)//step):
        sum = 0
        for i in range(step):
            sum += x[4*s+i]*(2**i)
        y.append(sum)
    return y
        
def bin_from_dec(y):
    x = []
    for i in range(len(y)):
        x += list(map(int, list(bin(y[i])[2:].zfill(4)[::-1])))
    return x

def random_x():
    return list(randint(2, size = 16))
        
def random_f():
    return list(permutation(16))

def inverse(f):
    g = []
    for i in range(len(f)):
        g.append(f.index(i))
    return g

def encode_row(x,f):
    d = dec_from_bin(x)
    y = []
    for i in range(len(d)):
        y.append(f[d[i]])
    y = bin_from_dec(y)
    y = rotate(y, y.count(1))
    return y
    

def print_vec(x):
    for i in range(len(x)):
        if x[i] == 0: print("O ", end = "")
        else: print("| ", end = "")
    print()
    
def print_vec_block(x):
    for i in range(len(x)):
        if x[i] == 0: print("  ", end = "")
        else: print("\u2588 ", end = "")
    print()
            
def permute_row(x,f):
    y = [0]*16
    for i in range(len(x)):
        y[f[i]] = x[i]
    return y

def encode_row(x,f):
    d = dec_from_bin(x)
    y = []
    for i in range(len(d)):
        y.append(f[d[i]])
    y = bin_from_dec(y)
    y = rotate(y, y.count(1))
    y = permute_row(y,f)
    return y
    
    
    
    


def print_vec(x):
    for i in range(len(x)):
        if x[i] == 0: print("O ", end = "")
        else: print("| ", end = "")
    print()
    
def print_vec_block(x):
    for i in range(len(x)):
        if x[i] == 0: print("  ", end = "")
        else: print("\u2588 ", end = "")
    print()
            
def encode(x,f):
    print_vec(x)
    for i in range(16):
        x = encode_row(x,rotate(f,i))
        print_vec(x) 
    return x

def decode_row(x,f):
    g = inverse(f)
    x = permute_row(x,g)
    x = rotate(x, -x.count(1))
    d = dec_from_bin(x)
    y = []
    for i in range(len(d)):
        y.append(g[d[i]])
    y = bin_from_dec(y)
    
    return y

def decode(x,f):
    print_vec(x)
    for i in range(16):
        x = decode_row(x,rotate(f,15 - i))
        print_vec(x) 
    return x
    
        
f = random_f()   
x = random_x();print_vec(x)    
y = encode(x,f); #print_vec(y)
print()
z = decode(y,f); #print_vec(z)
print()
print_vec(x)
print_vec(y)
print(x == z)
    
    