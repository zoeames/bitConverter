import math

def bin2dec(str): #converts binary to decimal
    a=list(str)
    s = 0
    for index, c in enumerate(reversed(a)):
        s += int(c)*(2**index)
    return s

f=bin2dec('1001')  #should get 9
print(f)
g=bin2dec('1100')  # should get 12
print(g)
h=bin2dec('1110')  # should get 12
print(h)


