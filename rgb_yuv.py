def rgb_yuv(r, g, b):
    y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    u = - 0.148 * r - 0.291 * g + 0.439 * b + 128
    v = 0.439 * r - 0.368 * g - 0.071 * b + 128
    print('This is Y', y, 'this U,', u, 'and this V', v)


def yuv_rgb(y, u, v):
    b = 1.164 * (y - 16) + 2.018 * (u - 128)
    g = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (u - 128)
    r = 1.164 * (y - 16) + 1.596 * (v - 128)
    print('This is R', r, 'this G,', g, 'and this B', b)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    R = int(input("Introduce value for R: "))
    G = int(input("Introduce value for G: "))
    B = int(input("Introduce value for B: "))
    Y = int(input("Introduce value for Y: "))
    U = int(input("Introduce value for U: "))
    V = int(input("Introduce value for V: "))
    rgb_yuv(R, G, B)
    yuv_rgb(Y, U, V)