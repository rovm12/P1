import numpy as np
from numpy import r_
import matplotlib.image as mpimg


def cosp(i,j,n): # This is the funky cos function inside the DCT
    output = 0
    output = np.cos(((2*i)+1)*j*np.pi/(2*n))
    return output


def dct(f, n, u, v, a, b): # This convolve function compute DCT for nxn @ axb location
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

if __name__ == '__main__':
    input_file = '/Users/ro/Desktop/pythonProject1/bw_lenna.png'
    f = mpimg.imread(input_file)
    print('image matrix size: ', f.shape)

    n = 8  # This will be the window in which we perform our DCT
    sumd = 0  # Initial value

    # Create some blank matrices in order to store our data
    dctmatrix = np.zeros(np.shape(f))  # Create a DCT matrix in which to plug our values
    f = f.astype(np.int16)  # Convert it so we can subtract 128 from each pixel
    f = f - 128  # The process commented above
    f2 = np.zeros(np.shape(f))  # We put the compressed image here

    # First we need to take into account our multiple nxn windows that jump across the image
    for a in r_[0:np.shape(f)[0]:n]:
        for b in r_[0:np.shape(f)[1]:n]:
            # Below, compute the DCT for a given uxv location in the DCT Matrix
            for u in r_[a:a + n]:
                for v in r_[b:b + n]:
                    dctmatrix[u, v] = dct(f, n, u, v, a, b)

    print("This is the DCT matrix", dctmatrix)

