def triangle_zhonxin(a, b, c):
    """ Returns the calculated center of gravity
        s of the triangle, in the form of tuple"""
    x = round((a[0] + b[0] + c[0]) / 3)     # x1 + x2 + x3
    y = round((a[1] + b[1] + c[1]) / 3)     # y1 + y2 + y3
    s = (x, y)      # class <tuple>
    return s
