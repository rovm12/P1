
# FUNCTIONS #
import numpy as np
from numpy import r_
import matplotlib.image as mpimg
import matplotlib as plt



def cosp(i,j,n): # This is the cosine function that we are going to use inside the DCT
    output = 0
    output = np.cos(((2*i)+1)*j*np.pi/(2*n))
    return output


def convolveDCT(f,n,u,v,a,b): # This convolve function compute the DCT
    sumd = 0                               # Initial value
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

# We are going to invert everything and, for that reason, define our inverse function

def convolveIDCT(dctmatrix,n,x,y,a,b): # This convolve function compute IDCT
    sumd = 0                               # Initial value
    for u in r_[0:n]:
        for v in r_[0:n]:
            val1 = 1
            val2 = 1
            x = x%n
            y = y%n
            if u == 0: val1 = 1/np.sqrt(2)
            if v == 0: val2 = 1/np.sqrt(2)
            sumd += dctmatrix[u+a,v+b]*val1*val2*cosp(x,u,n)*cosp(y,v,n)
    sumd *= 2/n
    return sumd


def dct_encoder():
    input_file = '/Users/ro/Desktop/pythonProject1/bw_lenna.png'
    f = mpimg.imread(input_file)
    print('image matrix size: ', f.shape)

    # Initialize some parameters

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
                    dctmatrix[u, v] = convolveDCT(f, n, u, v, a, b)

    # Let's take our first peek at the DCT
    np.around(dctmatrix)

    # Here, we will use a standard quantization table to compress the image stored
    Quant = np.array([
        [16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77],
        [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101],
        [72, 92, 95, 98, 112, 100, 103, 99]
    ])

    # As factor variable increases, the image will compress even more
    factor = 4
    for a in r_[0:np.shape(f)[0]:n]:
        for b in r_[0:np.shape(f)[1]:n]:
            dctmatrix[a:a + n, b:b + n] = dctmatrix[a:a + n, b:b + n] / Quant * factor

    # First we need to take into account our multiple nxn windows that jump across the image
    for a in r_[0:np.shape(dctmatrix)[0]:n]:
        for b in r_[0:np.shape(dctmatrix)[1]:n]:
            # Below, compute the IDCT for a given x,y location in the Image Matrix
            for x in r_[a:a + n]:
                for y in r_[b:b + n]:
                    f2[x, y] = convolveIDCT(dctmatrix, n, x, y, a, b)

    f2 = f2 + 128  # Scale our values back to 0-255 so we can see it through the screen

    return f2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    value = input("What type of photo do you have? (1 for color // 0 for black and white)")
    if value == "0":
        print("Perfect, let's continue!")
        dct_encoder()
    else:
        print("Not a correct type, try again.")