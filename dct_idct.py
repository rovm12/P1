
import numpy as np
from numpy import r_


def cosp(i,j,n): # This is the funky cos function inside the DCT
    output = 0
    output = np.cos(((2*i)+1)*j*np.pi/(2*n))
    return output


def convolveDCT(f,n,u,v,a,b): # This convolve function compute DCT for nxn @ axb location
    sumd = 0                               #INI value
    for x in r_[0:n]:
        for y in r_[0:n]:
            u = u%n
            v = v%n
            sumd += f[x+a,y+b]*cosp(x,u,n)*cosp(y,v,n)
    # Now, need to perform the functions outside of the sum values
    if u == 0: sumd *= 1/np.sqrt(2)
    else: sumd *= 1
    if v == 0: sumd *= 1/np.sqrt(2)
    else: sumd *= 1
    sumd *= 1/np.sqrt(2*n)
    return sumd


def convolveIDCT(dctmatrix,n,x,y,a,b): # This convolve function compute DCT for nxn @ axb location
    sumd = 0                               #INI value
    for u in r_[0:n]:
        for v in r_[0:n]:
            val1 = 1
            val2 = 1
            x = x%n
            y = y%n
            if u == 0: val1 = 1/np.sqrt(2)
            if v == 0: val2 = 1/np.sqrt(2)
            sumd += dctmatrix[u+a,v+b]*val1*val2*cosp(x,u,n)*cosp(y,v,n)
    # Now, need to perform the functions outside of the sum values
    sumd *= 2/n
    return sumd



