def rgb_yuv(r, g, b):
    y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    u = - 0.148 * r - 0.291 * g + 0.439 * b + 128
    v = 0.439 * r - 0.368 * g - 0.071 * b + 128
    print('This is Y', y, 'this U,', u, 'and this V', v)


def yuv_rgb(y, u, v):
    r = 1.164 * (y - 16) + 2.018 * (u - 128)
    g = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (u - 128)
    b = 1.164 * (y - 16) + 1.596 * (v - 128)
    print('This is R', r, 'this G,', g, 'and this B', b)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rgb_yuv(250, 30, 45)
    yuv_rgb(1, 1, 1)