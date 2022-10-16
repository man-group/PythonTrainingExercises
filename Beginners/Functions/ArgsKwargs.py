"""
Understanding Args and Kwargs

What will be the output from the following function calls
"""

def f(x, y, z):
    # uncomment for debug
    # print "x=%s y=%s, z=%s" % (x, y, z)
    return (x + y) / float(z)

print(f(10, 5, 3))

x = 20
y = 10
z = 3

# using kwargs
print(f(x=x, y=y, z=z))

# using args and kwargs
print(f(y, x, z=2))

# using args and kwargs out of order
print(f(z=3, y=x, x=y))

# all x
print(f(z=x, y=x, x=x))

"""
With defaults
"""

def ff(x=20, y=10, z=3):
    # uncomment for debug
    # print "x=%s y=%s, z=%s" % (x, y, z)
    return (x + y) / float(z)

print(ff(10, 5, 3))

# using args
print(ff(10))

# using kwargs
print(ff(z=10))

x = 20
print(ff(z=x, y=x))


